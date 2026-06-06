# LDA Topic Modeling Results

> 分析基於清理後資料（Reuters 標頭已移除），各類別各取 5,000 筆樣本進行 LDA 建模（n_topics=5）。

## Fake News Topics

| Topic | Top Keywords |
|-------|-------------|
| 1 | obama, president, people, american, america, states, united, world, said, country |
| 2 | said, police, year, gun, according, shooting, state, new, city, 000 |
| 3 | trump, twitter, people, just, donald, like, said, com, video, white |
| 4 | trump, republican, republicans, clinton, election, president, vote, said, party, hillary |
| 5 | trump, clinton, news, president, russia, said, hillary, media, realdonaldtrump, house |

## Real News Topics

| Topic | Top Keywords |
|-------|-------------|
| 1 | said, trump, united, president, china, states, trade, washington, north, korea |
| 2 | said, party, government, eu, year, percent, minister, european, election, political |
| 3 | said, military, state, government, north, security, people, russia, police, forces |
| 4 | said, court, state, law, government, states, federal, people, department, rights |
| 5 | trump, said, republican, house, president, clinton, campaign, senate, election, vote |

## 主題差異分析

| 面向 | Fake News | Real News |
|------|-----------|-----------|
| **主要詞彙** | `obama`, `twitter`, `video`, `com`, `realdonaldtrump` | `trade`, `eu`, `european`, `federal`, `security` |
| **敘事風格** | 情緒化、社群媒體傳播導向 | 政策導向、制度性語言 |
| **話題範圍** | 集中在陰謀論、個人攻擊、槍擊事件 | 涵蓋國際貿易、司法、政治選舉 |
| **地理範圍** | 偏美國內政 | 涵蓋歐盟、中國、北韓等國際議題 |

> 移除 Reuters 標頭後，Real News 主題中的 `reuters` 詞彙消失，
> 模型改從實質語意（政策詞彙、機構名稱、國際議題）學習真新聞特徵，
> 泛化能力顯著提升。
