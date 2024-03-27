mkdir -p ml_pipeline_project/config/projects
mkdir ml_pipeline_project/data
mkdir -p ml_pipeline_project/ml_pipeline/datasets
mkdir ml_pipeline_project/ml_pipeline/mixins
mkdir ml_pipeline_project/ml_pipeline/models
mkdir ml_pipeline_project/ml_pipeline/tests
mkdir ml_pipeline_project/tests
ls -R ml_pipeline_project

touch ml_pipeline_project/pipeline.py
touch ml_pipeline_project/config/common.yaml
touch ml_pipeline_project/config/datasets.yaml
touch ml_pipeline_project/config/projects/iris_classification.yaml

touch ml_pipeline_project/ml_pipeline/config.py
touch ml_pipeline_project/ml_pipeline/dataset.py
touch ml_pipeline_project/ml_pipeline/dataset_factory.py
touch ml_pipeline_project/ml_pipeline/model.py
touch ml_pipeline_project/ml_pipeline/model_factory.py
touch ml_pipeline_project/ml_pipeline/utils.py

touch ml_pipeline_project/ml_pipeline/datasets/iris.py

touch ml_pipeline_project/ml_pipeline/models/iris_classifier.py

touch ml_pipeline_project/ml_pipeline/mixins/csv_mixin.py
touch ml_pipeline_project/ml_pipeline/mixins/plotting_mixin.py
touch ml_pipeline_project/ml_pipeline/mixins/training_mixin.py

ls -R ml_pipeline_project