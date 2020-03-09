import logging
from common.workflow import *
from operators.vpcs.vpcs_operator import *
logger = logging.getLogger()

vpcs_opr = VpcOperator()

class GetExistingVpcs(WorkflowTask):

	def requires(self):
		logger.info("Requires {task}".format(task=self.__class__.__name__))
		return []

	def run(self):
		logger.info("Run {task}".format(task=self.__class__.__name__))
		vpcs_opr.query_existing_vpcs()
		self.finalize()

class CreateDefaultVpc(WorkflowTask):

	def requires(self):
		logger.info("Requires {task}".format(task=self.__class__.__name__))
		return [GetExistingVpcs(param=self.param)]

	def run(self):
		logger.info("Run {task}".format(task=self.__class__.__name__))
		vpcs_opr.create_default_vpc()
		self.finalize()

class VpcOperatorStart(WorkflowTask):

	def requires(self):
		logger.info("Requires {task}".format(task=self.__class__.__name__))
		return [CreateDefaultVpc(param=self.param)]

	def run(self):
		logger.info("Run {task}".format(task=self.__class__.__name__))
		self.finalize()