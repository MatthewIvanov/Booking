import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats 

data = pd.read_csv('Data/test.csv')

data_filtered = data[data.iloc[:, 1] < 120] 
data_filtered = data[data.iloc[:, 1] > 25]


print(data_filtered)

bins = [0, 30, 60, 90, 120]
labels = ['0-30', '31-60', '61-90', '91-120']

data_filtered['discrete'] = pd.cut(data_filtered.iloc[:, 1], bins=bins, labels=labels, right=False)

print(data_filtered)

#--------------------23--------------------

data = data_filtered.iloc[:, 1]

mu, std = np.mean(data), np.std(data)
print(f"Нормальное распределение: μ = {mu:.2f}, σ = {std:.2f}")

x_normal = np.linspace(mu - 3*std, mu + 3*std, 100)
y_normal = stats.norm.pdf(x_normal, mu, std)

lambda_param = 1 / np.mean(data)
print(f"Экспоненциальное распределение: λ = {lambda_param:.2f}")
x_exponential = np.linspace(0, max(data), 100)
y_exponential = stats.expon.pdf(x_exponential, scale=1/lambda_param)

n = 100
p = np.mean(data) / n
print(f"Биномиальное распределение: n = {n}, p = {p:.2f}")
x_binomial = np.arange(0, n+1)
y_binomial = stats.binom.pmf(x_binomial, n, p)

print(p)

lambda_poisson = np.mean(data)
print(f"Пуассоновское распределение: λ = {lambda_poisson:.2f}")
x_poisson = np.arange(0, int(max(data)) + 1)
y_poisson = stats.poisson.pmf(x_poisson, lambda_poisson)

# Визуализация
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
sns.histplot(data, bins=30, kde=True, stat='density', color='blue', label='Выборка')
plt.plot(x_normal, y_normal, 'r-', lw=2, label='Нормальное распределение')
plt.title('Приближение нормальным распределением')
plt.legend()

plt.subplot(2, 2, 2)
sns.histplot(data, bins=30, kde=True, stat='density', color='blue', label='Выборка')
plt.plot(x_exponential, y_exponential, 'g-', lw=2, label='Экспоненциальное распределение')
plt.title('Приближение экспоненциальным распределением')
plt.legend()

plt.subplot(2, 2, 3)
sns.histplot(data, bins=30, kde=True, stat='density', color='blue', label='Выборка')
plt.bar(x_binomial, y_binomial, color='purple', label='Биномиальное распределение')
plt.title('Приближение биномиальным распределением')
plt.legend()

plt.subplot(2, 2, 4)
sns.histplot(data, bins=30, kde=True, stat='density', color='blue', label='Выборка')
plt.bar(x_poisson, y_poisson, color='orange', label='Пуассоновское распределение')
plt.title('Приближение пуассоновским распределением')
plt.legend()

plt.tight_layout()
plt.show()

#--------------------------45-----------------------
bins = np.linspace(mu - 3*std, mu + 3*std, num=11)
observed_freq, _ = np.histogram(data, bins=bins)

bin_centers = 0.5 * (bins[:-1] + bins[1:])
expected_freq = len(data) * stats.norm.pdf(bin_centers, mu, std) * np.diff(bins)

expected_freq = expected_freq / expected_freq.sum() * sum(observed_freq)

print("Ожидаемые частоты (E_i):", expected_freq)

if len(observed_freq) != len(expected_freq):
    raise ValueError("Количество наблюдаемых и ожидаемых частот должно совпадать.")

print(f"Сумма наблюдаемых частот: {sum(observed_freq)}")
print(f"Сумма ожидаемых частот: {sum(expected_freq)}")

chi_squared_stat = np.sum((observed_freq - expected_freq) ** 2 / expected_freq)
df = len(observed_freq) - 1 - 2  # число интервалов - 1 - число оцениваемых параметров (μ, σ)

alpha = 0.05
critical_value = stats.chi2.ppf(1 - alpha, df)

# Результаты
print(f"Статистика Хи-квадрат: {chi_squared_stat:.2f}")
print(f"Критическое значение: {critical_value:.2f}")

if chi_squared_stat > critical_value:
    print("Не согласуются с нормальным распределением.")
else:
    print("Согласуются с нормальным распределением.")

#------------------6---------------------
# Готовая реализация Хи-квадрат теста
chi_squared_stat_builtin, p_value = stats.chisquare(observed_freq, expected_freq)

if p_value < alpha:
    print("Не согласуются с нормальным распределением.")
else:
    print("Согласуются с нормальным распределением.")