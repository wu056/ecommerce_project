{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d4718387-e690-43b6-b1d8-cf69ef8c6c73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: kagglehub in d:\\anaconda3\\lib\\site-packages (0.3.12)\n",
      "Requirement already satisfied: packaging in d:\\anaconda3\\lib\\site-packages (from kagglehub) (24.1)\n",
      "Requirement already satisfied: pyyaml in d:\\anaconda3\\lib\\site-packages (from kagglehub) (6.0.1)\n",
      "Requirement already satisfied: requests in d:\\anaconda3\\lib\\site-packages (from kagglehub) (2.32.3)\n",
      "Requirement already satisfied: tqdm in d:\\anaconda3\\lib\\site-packages (from kagglehub) (4.66.5)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in d:\\anaconda3\\lib\\site-packages (from requests->kagglehub) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in d:\\anaconda3\\lib\\site-packages (from requests->kagglehub) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in d:\\anaconda3\\lib\\site-packages (from requests->kagglehub) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in d:\\anaconda3\\lib\\site-packages (from requests->kagglehub) (2024.8.30)\n",
      "Requirement already satisfied: colorama in d:\\anaconda3\\lib\\site-packages (from tqdm->kagglehub) (0.4.6)\n"
     ]
    }
   ],
   "source": [
    "!pip install kagglehub"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ead7835e-99d6-4af6-9fca-2aea1ae4e874",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Path to dataset files: C:\\Users\\65299\\.cache\\kagglehub\\datasets\\thedevastator\\unlock-profits-with-e-commerce-sales-data\\versions\\2\n"
     ]
    }
   ],
   "source": [
    "import kagglehub\n",
    "\n",
    "# Download latest version\n",
    "path = kagglehub.dataset_download(\"thedevastator/unlock-profits-with-e-commerce-sales-data\")\n",
    "\n",
    "print(\"Path to dataset files:\", path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "60a1283b-9f7b-43e6-a31d-7f8e6a9f0c30",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import kagglehub"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "1a0f4409-81dc-415e-9907-5594c59ba30e",
   "metadata": {},
   "outputs": [],
   "source": [
    "file_path=r'C:\\Users\\65299\\.cache\\kagglehub\\datasets\\thedevastator\\unlock-profits-with-e-commerce-sales-data\\versions\\2\\Amazon Sale Report.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "4a12bf0b-4c0c-4ae8-90c7-3b28af9677f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "behavious=pd.read_csv(file_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "6975c553-0daf-4e5f-9bb0-bddc6fee5282",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Date</th>\n",
       "      <th>Status</th>\n",
       "      <th>ship-service-level</th>\n",
       "      <th>Category</th>\n",
       "      <th>Size</th>\n",
       "      <th>Amount</th>\n",
       "      <th>ship-city</th>\n",
       "      <th>ship-state</th>\n",
       "      <th>ship-postal-code</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>405-8078784-5731545</td>\n",
       "      <td>04-30-22</td>\n",
       "      <td>Cancelled</td>\n",
       "      <td>Standard</td>\n",
       "      <td>Set</td>\n",
       "      <td>S</td>\n",
       "      <td>647.62</td>\n",
       "      <td>MUMBAI</td>\n",
       "      <td>MAHARASHTRA</td>\n",
       "      <td>400081.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>171-9198151-1101146</td>\n",
       "      <td>04-30-22</td>\n",
       "      <td>Shipped - Delivered to Buyer</td>\n",
       "      <td>Standard</td>\n",
       "      <td>kurta</td>\n",
       "      <td>3XL</td>\n",
       "      <td>406.00</td>\n",
       "      <td>BENGALURU</td>\n",
       "      <td>KARNATAKA</td>\n",
       "      <td>560085.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>404-0687676-7273146</td>\n",
       "      <td>04-30-22</td>\n",
       "      <td>Shipped</td>\n",
       "      <td>Expedited</td>\n",
       "      <td>kurta</td>\n",
       "      <td>XL</td>\n",
       "      <td>329.00</td>\n",
       "      <td>NAVI MUMBAI</td>\n",
       "      <td>MAHARASHTRA</td>\n",
       "      <td>410210.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>403-9615377-8133951</td>\n",
       "      <td>04-30-22</td>\n",
       "      <td>Cancelled</td>\n",
       "      <td>Standard</td>\n",
       "      <td>Western Dress</td>\n",
       "      <td>L</td>\n",
       "      <td>753.33</td>\n",
       "      <td>PUDUCHERRY</td>\n",
       "      <td>PUDUCHERRY</td>\n",
       "      <td>605008.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>407-1069790-7240320</td>\n",
       "      <td>04-30-22</td>\n",
       "      <td>Shipped</td>\n",
       "      <td>Expedited</td>\n",
       "      <td>Top</td>\n",
       "      <td>3XL</td>\n",
       "      <td>574.00</td>\n",
       "      <td>CHENNAI</td>\n",
       "      <td>TAMIL NADU</td>\n",
       "      <td>600073.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128970</th>\n",
       "      <td>128970</td>\n",
       "      <td>406-6001380-7673107</td>\n",
       "      <td>05-31-22</td>\n",
       "      <td>Shipped</td>\n",
       "      <td>Expedited</td>\n",
       "      <td>kurta</td>\n",
       "      <td>XL</td>\n",
       "      <td>517.00</td>\n",
       "      <td>HYDERABAD</td>\n",
       "      <td>TELANGANA</td>\n",
       "      <td>500013.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128971</th>\n",
       "      <td>128971</td>\n",
       "      <td>402-9551604-7544318</td>\n",
       "      <td>05-31-22</td>\n",
       "      <td>Shipped</td>\n",
       "      <td>Expedited</td>\n",
       "      <td>Set</td>\n",
       "      <td>M</td>\n",
       "      <td>999.00</td>\n",
       "      <td>GURUGRAM</td>\n",
       "      <td>HARYANA</td>\n",
       "      <td>122004.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128972</th>\n",
       "      <td>128972</td>\n",
       "      <td>407-9547469-3152358</td>\n",
       "      <td>05-31-22</td>\n",
       "      <td>Shipped</td>\n",
       "      <td>Expedited</td>\n",
       "      <td>Western Dress</td>\n",
       "      <td>XXL</td>\n",
       "      <td>690.00</td>\n",
       "      <td>HYDERABAD</td>\n",
       "      <td>TELANGANA</td>\n",
       "      <td>500049.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128973</th>\n",
       "      <td>128973</td>\n",
       "      <td>402-6184140-0545956</td>\n",
       "      <td>05-31-22</td>\n",
       "      <td>Shipped</td>\n",
       "      <td>Expedited</td>\n",
       "      <td>Set</td>\n",
       "      <td>XS</td>\n",
       "      <td>1199.00</td>\n",
       "      <td>Halol</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>389350.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>128974</th>\n",
       "      <td>128974</td>\n",
       "      <td>408-7436540-8728312</td>\n",
       "      <td>05-31-22</td>\n",
       "      <td>Shipped</td>\n",
       "      <td>Expedited</td>\n",
       "      <td>Set</td>\n",
       "      <td>S</td>\n",
       "      <td>696.00</td>\n",
       "      <td>Raipur</td>\n",
       "      <td>CHHATTISGARH</td>\n",
       "      <td>492014.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>128975 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         index             Order ID      Date                        Status  \\\n",
       "0            0  405-8078784-5731545  04-30-22                     Cancelled   \n",
       "1            1  171-9198151-1101146  04-30-22  Shipped - Delivered to Buyer   \n",
       "2            2  404-0687676-7273146  04-30-22                       Shipped   \n",
       "3            3  403-9615377-8133951  04-30-22                     Cancelled   \n",
       "4            4  407-1069790-7240320  04-30-22                       Shipped   \n",
       "...        ...                  ...       ...                           ...   \n",
       "128970  128970  406-6001380-7673107  05-31-22                       Shipped   \n",
       "128971  128971  402-9551604-7544318  05-31-22                       Shipped   \n",
       "128972  128972  407-9547469-3152358  05-31-22                       Shipped   \n",
       "128973  128973  402-6184140-0545956  05-31-22                       Shipped   \n",
       "128974  128974  408-7436540-8728312  05-31-22                       Shipped   \n",
       "\n",
       "       ship-service-level       Category Size   Amount    ship-city  \\\n",
       "0                Standard            Set    S   647.62       MUMBAI   \n",
       "1                Standard          kurta  3XL   406.00    BENGALURU   \n",
       "2               Expedited          kurta   XL   329.00  NAVI MUMBAI   \n",
       "3                Standard  Western Dress    L   753.33   PUDUCHERRY   \n",
       "4               Expedited            Top  3XL   574.00      CHENNAI   \n",
       "...                   ...            ...  ...      ...          ...   \n",
       "128970          Expedited          kurta   XL   517.00    HYDERABAD   \n",
       "128971          Expedited            Set    M   999.00     GURUGRAM   \n",
       "128972          Expedited  Western Dress  XXL   690.00    HYDERABAD   \n",
       "128973          Expedited            Set   XS  1199.00        Halol   \n",
       "128974          Expedited            Set    S   696.00       Raipur   \n",
       "\n",
       "          ship-state  ship-postal-code  \n",
       "0        MAHARASHTRA          400081.0  \n",
       "1          KARNATAKA          560085.0  \n",
       "2        MAHARASHTRA          410210.0  \n",
       "3         PUDUCHERRY          605008.0  \n",
       "4         TAMIL NADU          600073.0  \n",
       "...              ...               ...  \n",
       "128970     TELANGANA          500013.0  \n",
       "128971       HARYANA          122004.0  \n",
       "128972     TELANGANA          500049.0  \n",
       "128973       Gujarat          389350.0  \n",
       "128974  CHHATTISGARH          492014.0  \n",
       "\n",
       "[128975 rows x 11 columns]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "behavious"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "4ca8eb48-2e8c-4c67-84b0-d927d7a40c99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "缺失值统计：\n",
      " 0         0\n",
      "1         0\n",
      "2         0\n",
      "3         0\n",
      "4         0\n",
      "         ..\n",
      "128970    0\n",
      "128971    0\n",
      "128972    0\n",
      "128973    0\n",
      "128974    0\n",
      "Length: 128975, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# 检测缺失值，查询每行有多少缺失值 \n",
    "missing_values = behavious.isnull().sum(1)  \n",
    "print(\"缺失值统计：\\n\", missing_values) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "9244d4aa-3092-4858-99ad-087e7de3805e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6819\n"
     ]
    }
   ],
   "source": [
    "# 检测重复交易（同一ID同一天购买同一品类）  \n",
    "mask = behavious.duplicated(subset=['Order ID','Date','Category'])  \n",
    "print(mask.sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "7d2858c0-873f-4a15-8004-9b4611e93924",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 删除重复值，保留首次记录  \n",
    "behavious_clean = behavious.drop_duplicates(subset=['Order ID','Date','Category'],keep='first')  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "536c87cd-5abe-499b-9e42-3a8a2b04ee8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#时间格式转化，原dataframe的切片副本，直接赋值修改格式会触发警告\n",
    "behavious_clean=behavious_clean.copy()#显式复制为独立DataFrame\n",
    "behavious_clean.loc[:,'Date']=pd.to_datetime(behavious_clean['Date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "a887a20e-f0b9-488c-916c-8bae77e9316c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "复购率：5.69%\n"
     ]
    }
   ],
   "source": [
    "# 计算各用户的购买次数\n",
    "purchase_counts = behavious['Order ID'].value_counts()\n",
    "# 定义复购用户：购买次数≥2次  \n",
    "repeat_purchase_users = purchase_counts[purchase_counts >= 2].count()  \n",
    "total_users = purchase_counts.count()  \n",
    "repeat_purchase_rate = repeat_purchase_users / total_users * 100  \n",
    "print(f\"复购率：{repeat_purchase_rate:.2f}%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "1d7ea82c-e945-4cd2-b84f-ea08547ea598",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "2715c26d-4af1-4b7e-b9b9-320df060acda",
   "metadata": {},
   "outputs": [],
   "source": [
    "#商品类别与复购频次分析"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "ef1eb60b-e150-475b-90a7-3989dabacaac",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. 计算每个用户对每个品类的购买次数\n",
    "user_category = behavious_clean.groupby(['Order ID', 'Category']).agg(\n",
    "    购买次数=('Date', 'count'),\n",
    "    首次购买=('Date', 'min'),\n",
    "    最近购买=('Date', 'max')\n",
    ").reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "5223d27f-30c9-4760-a297-0ce3a8f010fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2.计算购买间隔天数（最近购买 - 首次购买）\n",
    "user_category['购买间隔'] = (\n",
    "    user_category['最近购买'] - user_category['首次购买']\n",
    ").dt.days"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "efa7d338-1500-4642-a950-b084a66fe0e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "各商品类别消费频次统计：\n",
      "         Category  总复购用户数\n",
      "0         Blouse     897\n",
      "1         Bottom     410\n",
      "2        Dupatta       2\n",
      "3   Ethnic Dress    1148\n",
      "4          Saree     144\n",
      "5            Set   47845\n",
      "6            Top   10155\n",
      "7  Western Dress   14994\n",
      "8          kurta   46561\n"
     ]
    }
   ],
   "source": [
    "# 3. 筛选出购买次数≥1的用户（以便计算频次）\n",
    "repeat_users = user_category[user_category['购买次数'] >= 1].copy()\n",
    "\n",
    "# 4. 按商品类别汇总消费频次指标\n",
    "category_freq_stats = repeat_users.groupby('Category').agg(\n",
    "    总复购用户数=('Order ID', 'nunique'),\n",
    ").reset_index()\n",
    "\n",
    "# 5. 查看结果\n",
    "print(\"各商品类别消费频次统计：\\n\", category_freq_stats)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "c81db4b5-42c1-475e-b32a-4aa945b593af",
   "metadata": {},
   "outputs": [],
   "source": [
    "#筛选高金额（Amount > 500 ）且状态为已交付Delivered to Buyer ）的订单"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "dd182123-4886-4669-bd2d-8a5932dce012",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   Order ID  Amount       ship-city      ship-state\n",
      "14      408-1298370-1920302   771.0          MUMBAI     MAHARASHTRA\n",
      "15      403-4965581-9520319   544.0        GUNTAKAL  ANDHRA PRADESH\n",
      "25      405-8191138-5176316   582.0          RANCHI       JHARKHAND\n",
      "32      404-9632124-1107550  1233.0   VISAKHAPATNAM  ANDHRA PRADESH\n",
      "33      402-1465437-0579556   517.0          JEYPUR          ODISHA\n",
      "...                     ...     ...             ...             ...\n",
      "128865  407-7670498-3916345   625.0     NAVI MUMBAI     MAHARASHTRA\n",
      "128872  405-4724097-1016369   999.0           ALLUR  ANDHRA PRADESH\n",
      "128873  405-4724097-1016369  1523.0           ALLUR  ANDHRA PRADESH\n",
      "128887  405-6493630-8542756   518.0           NOIDA   UTTAR PRADESH\n",
      "128891  403-0317423-9322704   721.0  UTTAR BAGDOGRA     WEST BENGAL\n",
      "\n",
      "[17827 rows x 4 columns]\n"
     ]
    }
   ],
   "source": [
    "high_value_delivered = behavious_clean.loc[\n",
    "    (behavious_clean['Amount'] > 500) & \n",
    "    (behavious_clean['Status'] == 'Shipped - Delivered to Buyer'), \n",
    "    ['Order ID', 'Amount', 'ship-city', 'ship-state']  # 选取关注列\n",
    "]\n",
    "print(high_value_delivered)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "50ed9b42-f3ad-476d-bf73-385ffbc561f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                        Amount                                          \\\n",
      "Status               Cancelled   Pending Pending - Waiting for Pick Up   \n",
      "ship-service-level                                                       \n",
      "Expedited           3505684.00  244445.0                           0.0   \n",
      "Standard            3026731.53  150833.0                      181329.0   \n",
      "\n",
      "                                                                               \\\n",
      "Status                 Shipped Shipped - Damaged Shipped - Delivered to Buyer   \n",
      "ship-service-level                                                              \n",
      "Expedited           47777347.0               0.0                          0.0   \n",
      "Standard               33958.0            1136.0                   17620320.0   \n",
      "\n",
      "                                                                         \\\n",
      "Status             Shipped - Lost in Transit Shipped - Out for Delivery   \n",
      "ship-service-level                                                        \n",
      "Expedited                                0.0                        0.0   \n",
      "Standard                              1498.0                    25010.0   \n",
      "\n",
      "                                                                    ...  \\\n",
      "Status             Shipped - Picked Up Shipped - Rejected by Buyer  ...   \n",
      "ship-service-level                                                  ...   \n",
      "Expedited                          0.0                         0.0  ...   \n",
      "Standard                      628870.0                      7295.0  ...   \n",
      "\n",
      "                   Order ID                                                 \\\n",
      "Status              Shipped Shipped - Damaged Shipped - Delivered to Buyer   \n",
      "ship-service-level                                                           \n",
      "Expedited             72763                 0                            0   \n",
      "Standard               1024                 1                        27070   \n",
      "\n",
      "                                                                         \\\n",
      "Status             Shipped - Lost in Transit Shipped - Out for Delivery   \n",
      "ship-service-level                                                        \n",
      "Expedited                                  0                          0   \n",
      "Standard                                   4                         33   \n",
      "\n",
      "                                                                    \\\n",
      "Status             Shipped - Picked Up Shipped - Rejected by Buyer   \n",
      "ship-service-level                                                   \n",
      "Expedited                            0                           0   \n",
      "Standard                           928                          11   \n",
      "\n",
      "                                                                               \\\n",
      "Status             Shipped - Returned to Seller Shipped - Returning to Seller   \n",
      "ship-service-level                                                              \n",
      "Expedited                                     0                             0   \n",
      "Standard                                   1873                           132   \n",
      "\n",
      "                             \n",
      "Status             Shipping  \n",
      "ship-service-level           \n",
      "Expedited                 0  \n",
      "Standard                  8  \n",
      "\n",
      "[2 rows x 26 columns]\n"
     ]
    }
   ],
   "source": [
    "# 透视表：行是 ship-service-level ，列是 Status ，值统计订单数（count）和总金额（sum）\n",
    "pivot_service_status = behavious_clean.pivot_table(\n",
    "    index='ship-service-level', \n",
    "    columns='Status', \n",
    "    values=['Order ID', 'Amount'], \n",
    "    aggfunc={'Order ID': 'count', 'Amount': 'sum'},\n",
    "    fill_value=0  # 空值填 0\n",
    ")\n",
    "print(pivot_service_status)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b46f9e52-e467-455a-b5a3-eb780e3af96f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
