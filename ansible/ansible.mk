ansible-provision:
	@echo "---------- Provisioning EC2 instance ----------"
	{ \
		cd ansible ; \
		ansible-playbook --ask-become-pass playbooks/bootstrap.yml ; \
	}
	@echo "------- Finished Instance Provisioning --------"

ansible-runner-config:
	@echo "----------- Configuring Runner ------------------"
	{ \
		cd ansible ; \
		./set_runner_token.sh ; \
		ansible-playbook playbooks/runner.yml ; \
	}
	@echo "---------- Finished Runner configuration ---------"

ansible-all: ansible-provision ansible-runner-config