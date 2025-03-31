import pickle
from sklearn.svm import SVC
import numpy as np

def train_contract_classifier():
    """Train a contract classifier."""
    with open("models/embeddings.pkl", "rb") as f:
        embeddings = pickle.load(f)
    labels = np.random.choice(["NDA", "Vendor", "Employment", "Lease", "M&A"], size=len(embeddings))
    classifier = SVC(kernel="linear")
    classifier.fit(embeddings, labels)
    with open("models/classifier.pkl", "wb") as f:
        pickle.dump(classifier, f)

if __name__ == "__main__":
    train_contract_classifier()
