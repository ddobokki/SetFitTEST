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