import random

from datasets import load_dataset
from sentence_transformers.losses import CosineSimilarityLoss
from setfit import SetFitModel, SetFitTrainer
from sklearn.metrics.pairwise import cosine_distances

dataset = load_dataset("nsmc")
eval_dataset = dataset["test"]

model = SetFitModel.from_pretrained("ddobokki/klue-roberta-base-nli-sts")

train_dataset = dataset["train"]

trainer = SetFitTrainer(
    model=model,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    loss_class=CosineSimilarityLoss,
    metric="accuracy",
    batch_size=16,
    num_iterations=1, # The number of text pairs to generate for contrastive learning
    num_epochs=1, # The number of epochs to use for constrastive learning
    column_mapping={'document': 'text', "label": "label"} # Map dataset columns to text/label expected by trainer
)
trainer.train()
metrics = trainer.evaluate()
print(metrics)


# model = SetFitModel.from_pretrained("ddobokki/klue-roberta-base-nli-sts")
# n_iter = 20

# for n in range(20):
#     train_dataset = train_dataset.shuffle().select(range(40))
#     trainer = SetFitTrainer(
#         model=model,
#         train_dataset=train_dataset,
#         eval_dataset=eval_dataset,
#         loss_class=CosineSimilarityLoss,
#         metric="accuracy",
#         batch_size=16,
#         num_iterations=2, # The number of text pairs to generate for contrastive learning
#         num_epochs=1, # The number of epochs to use for constrastive learning
#         column_mapping={'document': 'text', "label": "label"} # Map dataset columns to text/label expected by trainer
#     )
#     trainer.train()
#     metrics = trainer.evaluate()
#     print(metrics)
