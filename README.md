# Tutorial Instructions

#### Docker Method (Preferred Method)

Download the following from `dockerhub` `westhealth/scipy2022-missingness-tutorial`

```docker pull westhealth/scipy2022-missingness-tutorial```

#### Colab Compatible Method

Versions designed for google colaboratory are available at: https://github/Westhealth/scipy2022-missingness-tutorial/tree/main/colab.

Since colab isolates every notebook in it's own VM, to reduce the amount of file uploading, it is recommended that you create a folder in your google drive called `missingness_tutorial` so that the notebooks can share files.

#### Build Your Own

If you intend to build this yourself, the docker container uses the following:

| Library     | Version |
| ----------- | ------- |
|             |         |
| python      | 3.9.7   |
| tensorflow  | 2.6.2   |
| pandas      | 1.4.0   |
| autoimpute* | 0.12.3  |
| numpy       | 1.22.1  |
| scipy       | 1.7.3   |
| sklearn     | 1.0.2   |
| missingno   | 0.4.2   |

For autoimpute to work properly gcc and g++ must be installed.