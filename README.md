# SetFitTEST
- 간단하게...
```
python3.8 -m venv .venv

pip install --upgrade pip
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
pip install -r requirments.txt
```

# NSMC
- 42 * 2 개를 랜덤 샘플링
- 'accuracy': 0.80988
- 오오...!

# 만약 FewShot이 아니라 전부 다 사용하고 싶으면?
- 데이터 구성방식이 pos_pair, neg_pair를 num_iterations 개 만큼 만들어 contrastive learning을 하는 형식
- 만약 15만개라면 1개로 구성한다고 해도 최소 30만개에 대해 학습해야함

## 그래서 말이죠?
- 전체 데이터에서 n번, k개씩 샘플링해서 반복해 학습을 하면....?-> 테스트중
- 오르나...?

## 실험 방법
- nsmc에서 train data를 400개를 샘플링 및 학습(n_iter=20) -> 0.81596
- 위에서 추출한 400개를 고정시킴
- 데이터를 랜덤 샘플링으로 40개를 뽑고 학습을 20번 반복(n_iter=2) -> 0.75 ~ 0.78 왔다 갔다...

# 미친척하고 NSMC 전부 다 돌려봄
- 'accuracy': 0.9075 ...?!