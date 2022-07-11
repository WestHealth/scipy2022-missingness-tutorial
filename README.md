# Tutorial Instructions

#### Binder (Preferred Method)

Just follow this link: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/WestHealth/scipy2022-missingness-tutorial/main)

#### Docker Method (Preferred Method)

Download the following from `dockerhub` `westhealth/scipy2022-missingness-tutorial`

```docker pull westhealth/scipy2022-missingness-tutorial```

This notebook is built onto of the standard `jupyter` docker images which require hash authentication. The hash is found in the output of the docker container. If for some reason you cannot find this you can pull an "insecure" version of the docker image where there authentication is turned off. While risk is minimal, lack of authentication means it is theoretically possible for someone to access your container.  If you elect the insecure option, download it from dockerhub:

```docker pull westhealth/scipy2022-missingness-tutorial:insecure```

You may also elect to build your from this Github Repository:  https://github/Westhealth/scipy2022-missingness-tutorial/

#### Colab Compatible Method

Versions designed for google colaboratory are available at: https://github/Westhealth/scipy2022-missingness-tutorial/tree/main/colab.

Since colab isolates every notebook in it's own VM, to reduce the amount of file uploading, it is recommended that you create a folder in your google drive called `missingness_tutorial` so that the notebooks can share files. It is recommended as well that you upload the `helpers.py` file and the `data` folder into this `missingness_tutorial` folder.

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
