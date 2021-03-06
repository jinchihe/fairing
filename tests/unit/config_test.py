"""Tests for Fairing configuration options."""

import pytest
from unittest.mock import patch
import fairing.config as config

from fairing.preprocessors.base import BasePreProcessor
from fairing.preprocessors.converted_notebook import ConvertNotebookPreprocessor

from fairing.builders.append.append import AppendBuilder
from fairing.builders.docker.docker import DockerBuilder

from fairing.deployers.job.job import Job
from fairing.deployers.tfjob.tfjob import TfJob

def test_set_preprocessor():
    """Assert that a custom preprocessor can be provided."""
    config.reset()
    config.set_preprocessor('notebook')
    assert isinstance(config.get_preprocessor(), ConvertNotebookPreprocessor)

def test_get_preprocessor_with_default():
    """
    Assert that getting the preprocessor without setting it returns the default
    preprocessor.
    """
    config.reset()
    assert isinstance(config.get_preprocessor(), BasePreProcessor)

def test_set_builder_default():
    """
    Assert that the default builder is set when no explicit argument is
    provided.
    """
    config.reset()
    config.set_builder(push=False)
    assert isinstance(config.get_builder(config.get_preprocessor()), AppendBuilder)

def test_set_builder():
    """Assert that a custom builder can be provided."""
    config.reset()
    config.set_builder('docker', push=False)
    assert isinstance(config.get_builder(config.get_preprocessor()), DockerBuilder)
