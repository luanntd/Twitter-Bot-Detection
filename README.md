# **Twitter-Bot-Detection**
This is a project of me and my friends for the subject. It marks our first steps into the field of Machine Learning. 
![twitter-bot](https://developers.moralis.com/wp-content/uploads/2024/06/Blog-Twitter-Bot-1024x397.png)

## **Description**
The project aims to detect non-human accounts from the **Twitter(X)** platform with basic techniques in **ML** using the **User Information**.

### **Technologies**
- **Data Processing**: Numpy, Pandas
- **Data Visualization**: Matplotlib, Seaborn
- **ML Tool**: Scikit-learn, Yellowbrick, Imblearn, Hyperopt
- **ML Models**: Random Forest, LightGBM, Catboost
- **Metrics**: Precision, Recall, F1

### **Dependencies**
All the required packages are listed in requirements.txt. To install all the dependencies, run
```bash
pip install -r requirements.txt
```

## **Dataset**
The dataset consists of various samples containing both human and non-human account. It is divided into following files:

| **File**      | **Description** |
|---------------|-----------------|
| user.json | User account Information |
| label.csv | Human or Bot |

Dataset at [data-source](https://twibot22.github.io/).
Paper at [paper-source](https://arxiv.org/abs/2206.04564).

## **Performance**
We prioritize high **recall** results due to domain specificity, so the following results are on the Bot label.

| **Model**      | **Precision** | **Recall** | **F1** |
|---------------|-----------------|----------|-----------|
| Random Forest | 0.48 | 0.49 | 0.49 |
| LightGBM | 0.31 | 0.83 | 0.45 |
| Catboost | 0.32 | 0.82 | 0.46 |

### **Overall**

| **Model**      | **Accuracy** | **F1-macro** |
|---------------|-----------------|----------|
| Random Forest | 85% | 70% |
| LightGBM | 72% | 63% |
| Catboost | 73% | 64% |

## Collaborators

<a href="https://github.com/luanntd">
  <img src="https://github.com/luanntd.png?size=60" width="60" style="border-radius: 50%;" />
</a>
<a href="https://github.com/Khoa-Nguyen-Truong">
  <img src="https://github.com/Khoa-Nguyen-Truong.png?size=60" width="60" style="border-radius: 50%;" />
</a>
<a href="https://github.com/KHann-71">
  <img src="https://github.com/KHann-71.png?size=60" width="60" style="border-radius: 50%;" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
