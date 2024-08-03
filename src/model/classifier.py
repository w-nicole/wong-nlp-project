from typing import List, Optional, Type

import torch.nn as nn
import torch.nn.functional as F

from dataset import Dataset, LanguageID, MLDoc, PawsX, Xnli
from enumeration import Split, Task
from metric import AccuracyMetric
from model.base import Model


class Classifier(Model):
    def __init__(self, hparams):
        super(Classifier, self).__init__(hparams)

        self._comparsion = {
            Task.xnli: "max",
            Task.pawsx: "max",
            Task.mldoc: "max",
            Task.langid: "max",
        }[self.hparams.task]
        self._selection_criterion = {
            Task.xnli: "val_acc",
            Task.pawsx: "val_acc",
            Task.mldoc: "val_acc",
            Task.langid: "val_acc",
        }[self.hparams.task]
        self._nb_labels: Optional[int] = None
        self._nb_labels = {
            Task.xnli: Xnli.nb_labels(),
            Task.pawsx: PawsX.nb_labels(),
            Task.mldoc: MLDoc.nb_labels(),
            Task.langid: LanguageID.nb_labels(),
        }[self.hparams.task]
        self._metric = {
            Task.xnli: AccuracyMetric(),
            Task.pawsx: AccuracyMetric(),
            Task.mldoc: AccuracyMetric(),
            Task.langid: AccuracyMetric(),
        }[self.hparams.task]

        self.classifier = nn.Linear(self.hidden_size, self.nb_labels)
        self.padding = {
            "sent": self.tokenizer.pad_token_id,
            "segment": 0,
            "label": 0,
            "lang": 0,
        }

        self.setup_metrics()

    @property
    def nb_labels(self):
        assert self._nb_labels is not None
        return self._nb_labels

    def preprocess_batch(self, batch):
        batch["label"] = batch["label"].view(-1)
        return batch

    def forward(self, batch):
        batch = self.preprocess_batch(batch)
        hs = self.encode_sent(batch["sent"], batch["lang"], segment=batch["segment"])
        if hs.dim() == 3:
            hs = hs[:, 0]
        logits = self.classifier(hs)
        log_probs = F.log_softmax(logits, dim=-1)

        loss = F.nll_loss(log_probs.view(-1, self.nb_labels), batch["label"])
        return loss, log_probs

    def training_step(self, batch, batch_idx):
        loss, _ = self.forward(batch)
        self.log("loss", loss)
        return loss

    def evaluation_step_helper(self, batch, prefix):
        loss, log_probs = self.forward(batch)

        assert (
            len(set(batch["lang"])) == 1
        ), "eval batch should contain only one language"
        lang = batch["lang"][0]
        self.metrics[lang].add(batch["label"], log_probs)

        result = dict()
        result[f"{prefix}_{lang}_loss"] = loss
        return result

    def prepare_datasets(self, split: str) -> List[Dataset]:
        hparams = self.hparams
        data_class: Type[Dataset]
        if hparams.task == Task.xnli:
            data_class = Xnli
        elif hparams.task == Task.pawsx:
            data_class = PawsX
        elif hparams.task == Task.mldoc:
            data_class = MLDoc
        elif hparams.task == Task.langid:
            data_class = LanguageID
        else:
            raise ValueError(f"Unsupported task: {hparams.task}")

        if split == Split.train:
            return self.prepare_datasets_helper(
                data_class, hparams.trn_langs, Split.train, hparams.max_trn_len
            )
        elif split == Split.dev:
            return self.prepare_datasets_helper(
                data_class, hparams.val_langs, Split.dev, hparams.max_tst_len
            )
        elif split == Split.test:
            return self.prepare_datasets_helper(
                data_class, hparams.tst_langs, Split.test, hparams.max_tst_len
            )
        else:
            raise ValueError(f"Unsupported split: {hparams.split}")

    @classmethod
    def add_model_specific_args(cls, parser):
        return parser
