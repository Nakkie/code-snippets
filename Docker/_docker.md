# Docker Readme

    I am by no means an expert when it comes to docker, this is mostly for my own ease reference

Below are descriptions for the files contained in this directory

## docker_mysql_db_extract

For dumping out a db dump file from a docker image

Basic copy command

## extract_env_docker

This is for extract env from a linux image

We were migrating Github repositories between domains, Github actions was referencing secrets that weren't stored in our 1pass, yeah, so had to spin up each image and extract the envs for migration to the new domain