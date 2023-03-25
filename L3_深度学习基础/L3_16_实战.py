#数据预处理
#对连续数值的特征做标准化，设该特征在整个数据集上的均值为μ，标准差为σ。那么，我们可以将该特征的每个值先减去μ再除以σ得到标准化后的每个特征值
#将离散数值转成指示特征，假设特征MSZoning里面有两个不同的离散值RL和RM，那么这一步转换将去掉MSZoning特征，并新加两个特征MSZoning_RL和MSZoning_RM，其值为0或1。
#最后，通过values属性得到NumPy格式的数据，并转成Tensor方便后面的训练。