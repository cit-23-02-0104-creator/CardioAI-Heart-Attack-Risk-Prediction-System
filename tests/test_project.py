import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.train import FEATURES, TARGET, load_data, build_models


class ProjectTests(unittest.TestCase):
    def test_dataset_schema(self):
        df = load_data()
        self.assertEqual(len(df), 1000)
        self.assertTrue(all(c in df.columns for c in FEATURES + [TARGET]))
        self.assertTrue(df[TARGET].isin([0, 1]).all())

    def test_models_build(self):
        models = build_models()
        self.assertEqual(len(models), 4)
        self.assertEqual(
            set(models),
            {"Logistic Regression", "Decision Tree", "Random Forest", "XGBoost"},
        )


if __name__ == "__main__":
    unittest.main()
