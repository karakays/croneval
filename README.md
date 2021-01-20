# croneval

`croneval` is a POSIX compliant cron evaluator. It can describe cron expressions by printing datetime fields that
given schedule expression resolves to.

## Dependencies

Python interpreter 3.8

## Install with docker

```buildoutcfg
$ docker run -it karakays/croneval croneval "* * * * * find"
```

## Install with pip

```buildoutcfg
$ git clone https://github.com/karakays/croneval.git && cd croneval
$ pip install .
```

## Usage

```buildoutcfg
$ croneval "* * * * * /usr/bin/find"
```
## Authors

Selçuk Karakayalı <skarakayali@gmail.com>

