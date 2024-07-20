import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class EnergyAnalyzer:
    def __init__(self):
        self.pca = PCA(n_components=2)
        self.kmeans = KMeans(n_clusters=5)

    def analyze(self, data: pd.DataFrame):
        X = data.drop(['energy_consumption'], axis=1)
        X_pca = self.pca.fit_transform(X)
        clusters = self.kmeans.fit_predict(X_pca)

        return clusters

energy_analyzer = EnergyAnalyzer()
