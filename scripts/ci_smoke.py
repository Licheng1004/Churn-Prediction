"""Run a tiny, data-independent LightGBM training smoke check."""
import numpy as np
from lightgbm import LGBMClassifier

X = np.array([[i, i % 4, (i * 3) % 7] for i in range(32)], dtype=np.float32)
y = np.array([0, 1] * 16, dtype=np.int32)
model = LGBMClassifier(
    n_estimators=5,
    num_leaves=4,
    min_child_samples=2,
    n_jobs=1,
    random_state=0,
    verbosity=-1,
)
model.fit(X, y)
probabilities = model.predict_proba(X)
assert probabilities.shape == (len(y), 2)
assert np.isfinite(probabilities).all()
print('LightGBM synthetic training smoke check passed.')
