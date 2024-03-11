## Steps to run Code

1. Clone the repository

2. Go to the Cloned Folder by entering the command on terminal:
    ```
    cd Traffic-Analysis
    ```
3. Now Install the Dependencies by entering:
    ```
    pip install -e '.[dev]'
    ```
4. Download DeepSORT File To the Directory

5. Finally Run The Program By entering:
    ```
    python predict.py model=yolov8l.pt source="<Your Video Name/ source >" show=True
    ```