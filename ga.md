---

=== Question 1

In GitHub Actions, how is the success or failure of a step determined by its exit code?

* [ ] A.	Exit codes are ignored and a maintainer sets the result manually
* [ ] B.	Zero exit code means success and any nonzero means failure
* [ ] C.	Success is controlled by continue-on-error rather than the exit code
* [ ] D.	Every exit code is a failure

=== Question 2

Which configuration lines correctly set the workflow name in a GitHub Actions workflow file? (Choose 2)

* [ ] A.	name: $ &quot;release-flow-42&quot; 
* [ ] B.	name: $ &apos;release-flow-42&apos; 
* [ ] C.	run-name: release-flow-42
* [ ] D.	name: release-flow-42

=== Question 3

In GitHub Enterprise Cloud, where do you set the policy that allows only enterprise hosted actions and reusable workflows to run?

* [ ] A.	Organization settings Policies then Actions
* [ ] B.	Enterprise account Actions policy
* [ ] C.	Repository settings Actions general

=== Question 4

In GitHub Actions, where should you declare custom environment variables so they are accessible across all jobs and steps in a single workflow run?

* [ ] A.	Repository variables
* [ ] B.	Set env in the workflow YAML
* [ ] C.	Environment secrets
* [ ] D.	Runner command line arguments

=== Question 5

Which GitHub Actions event configuration triggers only for pull requests targeting the release branch and not for push events?

* [ ] A.	on: pull_request_target: branches: - release
* [ ] B.	on: pull_request: branches: - release
* [ ] C.	on: push: branches: - release
* [ ] D.	on: pull_request: types: - opened

=== Question 6

In GitHub Actions, which workflow key defines the events that trigger the workflow such as push or pull_request?

* [ ] A.	if:
* [ ] B.	on:
* [ ] C.	env:
* [ ] D.	jobs:

=== Question 7

What repository visibility is required for a GitHub Action to be listed on GitHub Marketplace?

* [ ] A.	Verified creator status
* [ ] B.	Metadata in a subfolder
* [ ] C.	Public repository
* [ ] D.	Use GitHub Container Registry

=== Question 8

Which GitHub Actions capability prevents secrets from appearing in workflow logs?

* [ ] A.	Manual approval for secret log output
* [ ] B.	GitHub Audit Log
* [ ] C.	Default secret masking in logs
* [ ] D.	Encrypted secrets written to logs

=== Question 9

In a workflow triggered by a pull request comment, which GitHub Actions context property contains the event payload used to access the comment text and the pull request number?

* [ ] A.	github.repository
* [ ] B.	github.event
* [ ] C.	github.event_path
* [ ] D.	github.job

=== Question 10

Which repository files are required for a Docker container action and for a JavaScript action to run correctly? (Choose 3)

* [ ] A.	JavaScript entry file such as main.js or index.js
* [ ] B.	package.json
* [ ] C.	Action metadata file action.yml or action.yaml
* [ ] D.	Container action Dockerfile

=== Question 11

Which type of GitHub Actions runner gives you full control over the execution environment for proprietary tools and supports elastic scaling?

* [ ] A.	GitHub hosted runners
* [ ] B.	Self hosted runners on virtual machines you manage
* [ ] C.	GitHub Actions larger runners
* [ ] D.	GitHub Codespaces

=== Question 12

In GitHub Actions, what is the correct relationship among events, workflows, jobs, steps, and actions?

* [ ] A.	A repository_dispatch starts the pipeline and the workflow runs actions directly without jobs or steps
* [ ] B.	Jobs hold one or more actions and workflows are collections of steps across jobs
* [ ] C.	An event triggers a workflow that runs one or more jobs and each job has steps that use actions
* [ ] D.	Steps start actions and actions start workflows that run jobs

=== Question 13

In a custom GitHub Action, which metadata key is used to expose values to subsequent workflow steps?

* [ ] A.	runs
* [ ] B.	outputs
* [ ] C.	branding
* [ ] D.	inputs

=== Question 14

In GitHub Actions, why is it better for workflows to reference file paths using variables rather than hardcoded paths when running on hosted and self hosted runners?

* [ ] A.	GitHub Actions blocks hardcoded paths
* [ ] B.	Variables let workflows adapt to different runner paths
* [ ] C.	GITHUB_WORKSPACE is the same on all runners so fixed paths are safe

=== Question 15

What is the best way to publish a reusable GitHub Action that accepts multiple inputs to ensure wide discoverability and a clear contract for consumers?

* [ ] A.	Publish only to GitHub Container Registry
* [ ] B.	Public repository with action metadata and Marketplace listing
* [ ] C.	Public repo and README only

=== Question 16

In the Actions view, which filter displays only runs that were triggered by pull request events?

* [ ] A.	Branch
* [ ] B.	Workflow
* [ ] C.	Event

=== Question 17

Under what circumstances should a team choose GitHub hosted runners to minimize maintenance and enable rapid onboarding?

* [ ] A.	when they need job traffic to come from fixed IP addresses for firewall allowlists
* [ ] B.	when they want GitHub to provide ephemeral runners that scale automatically with no setup
* [ ] C.	when they require root access and complete control of the runner environment for compliance

=== Question 18

In GitHub Actions, which feature allows you to target specific self-hosted runners for jobs without naming individual runners?

* [ ] A.	environments
* [ ] B.	runner labels
* [ ] C.	matrix strategy
* [ ] D.	runner groups

=== Question 19

In a GitHub Actions step that runs shell commands, which command writes a debug message to the job log?

* [ ] A.	echo &quot;::notice::start bootstrap script&quot;
* [ ] B.	echo &quot;::debug::start bootstrap script&quot;
* [ ] C.	set -x
* [ ] D.	Set ACTIONS_STEP_DEBUG to true in repository secrets

=== Question 20

Within a GitHub repository, where are the GitHub Actions workflow YAML files stored?

* [ ] A.	the Actions tab in the repository
* [ ] B.	the .github/workflows directory
* [ ] C.	the .github/actions directory

=== Question 21

In a GitHub Actions status badge URL, how can you limit the badge to show only workflow runs triggered by the push event?

* [ ] A.	GitHub Pages
* [ ] B.	Add ?event=push to the badge URL
* [ ] C.	Use the branch name as the event parameter in the badge URL
* [ ] D.	Change the on section of the workflow file to only include the push trigger

=== Question 22

Which naming strategy for shared GitHub Actions components across repositories best supports discovery, reuse, and versioning?

* [ ] A.	Rely on repository topics and code search for discovery instead of standardizing names
* [ ] B.	Use repository releases and tags for versioning but skip naming conventions
* [ ] C.	Adopt and enforce a unified naming convention that encodes component type purpose and version
* [ ] D.	Allow each product team to define its own naming pattern for reusable components

=== Question 23

To maximize discoverability and adoption by external maintainers, where should you publish a reusable GitHub Action?

* [ ] A.	GitHub Packages
* [ ] B.	GitHub Marketplace
* [ ] C.	A public GitHub repository

=== Question 24

In a GitHub Actions workflow for integration tests that depend on PostgreSQL and Redis, what is the primary advantage of using service containers?

* [ ] A.	Dependency caching with actions/cache
* [ ] B.	Run dependent services as ephemeral containers in the job
* [ ] C.	Faster code compilation during build steps
* [ ] D.	Automatic code vulnerability detection during the pipeline

=== Question 25

To help other teams quickly adopt a reusable GitHub Action, what is the first piece of documentation you should create?

* [ ] A.	Publish to GitHub Marketplace
* [ ] B.	Create a clear README with description, inputs, outputs, secrets, and examples
* [ ] C.	Build an interactive setup walkthrough
* [ ] D.	Compile a full feature catalog

=== Question 26

In GitHub Actions, what is the main purpose of workflow commands issued within a run step?

* [ ] A.	Run custom scripts on the runner
* [ ] B.	Set environment variables for the whole workflow
* [ ] C.	Send directives and metadata to the runner
* [ ] D.	Trigger another workflow

=== Question 27

What is the best way to structure reusable GitHub Actions workflows to provide consistent CI across more than 60 repositories while ensuring they are versioned and easy to maintain?

* [ ] A.	Starter Workflows in the .github repository
* [ ] B.	Use branches and tags for workflows in each repository
* [ ] C.	Central repository workflows invoked with workflow_call and version tags

=== Question 28

In GitHub Actions, how can you configure a workflow to run only on weekdays Monday through Friday?

* [ ] A.	Add a job level if that checks the weekday and skips Saturday and Sunday
* [ ] B.	Use a cron expression in the schedule event that matches weekdays only
* [ ] C.	Invoke workflow_dispatch on weekdays using Azure Logic Apps

=== Question 29

In a GitHub repository, where must YAML workflow files be located for GitHub Actions to automatically detect and run them?

* [ ] A.	.github/pipelines
* [ ] B.	.github/workflows
* [ ] C.	github/workflows

=== Question 30

In a GitHub Actions workflow with two pwsh steps where the first step runs two commands and the second runs one, how many PowerShell commands execute on the Windows runner?

* [ ] A.	4
* [ ] B.	2
* [ ] C.	3
* [ ] D.	5

=== Question 31

In a private GitHub repository, which repository permission is required to delete archived GitHub Actions workflow run logs?

* [ ] A.	admin
* [ ] B.	write
* [ ] C.	maintain
* [ ] D.	read

=== Question 32

A GitHub Actions workflow contains jobs and steps, but it never runs when commits are pushed to the main branch. Which configuration mistake would prevent it from triggering?

* [ ] A.	YAML indentation is malformed
* [ ] B.	Workflow lacks an on trigger so no event starts it
* [ ] C.	The workflow file is outside .github/workflows
* [ ] D.	Each run step must have a unique id

=== Question 33

Within a GitHub Actions workflow, what does the GITHUB_ACTIONS environment variable indicate?

* [ ] A.	It holds the REST API base URL
* [ ] B.	It is set to &quot;true&quot; only when running on GitHub Actions
* [ ] C.	It contains the current run ID

=== Question 34

In GitHub Actions, which capability packages multiple steps into a single reusable unit without using Docker or custom JavaScript?

* [ ] A.	Reusable workflows
* [ ] B.	Composite action that groups steps
* [ ] C.	Docker action
* [ ] D.	JavaScript action

=== Question 35

In a GitHub Actions workflow, what does the jobs.build_app.runs-on setting specify?

* [ ] A.	It defines job level environment variables
* [ ] B.	It selects the runner environment and operating system for the job
* [ ] C.	It sets the strategy matrix for parallel builds

=== Question 36

In GitHub, where can you view the run logs to troubleshoot a failed Actions workflow on a pull request? (Choose 2)

* [ ] A.	Security
* [ ] B.	Pull request &quot;Checks&quot; tab
* [ ] C.	Repository &quot;Actions&quot; tab
* [ ] D.	Issues

=== Question 37

In a single GitHub Actions workflow, how do you define job dependencies so that qa runs after compile and release runs after qa?

* [ ] A.	Configure a workflow_run trigger
* [ ] B.	Set job dependencies with needs on dependent jobs
* [ ] C.	Use an if condition with success() on each job

=== Question 38

How does the packaging and distribution of JavaScript GitHub Actions differ from that of typical Node.js applications?

* [ ] A.	Published to npm and installed at runtime
* [ ] B.	They can only call GitHub APIs and cannot reach external services
* [ ] C.	Dependencies are bundled and committed, and releases are tagged for GitHub Marketplace
* [ ] D.	They are packaged by Cloud Build and delivered through Artifact Registry

=== Question 39

After renaming environment variables, a GitHub Actions workflow fails. What should you check first to diagnose the issue?

* [ ] A.	Enable step debug logging with ACTIONS_STEP_DEBUG and rerun
* [ ] B.	Review run logs and repository documentation to confirm how variables are defined and passed
* [ ] C.	Rotate the cloud provider service account key and redeploy

=== Question 40

Which GitHub Actions event triggers a workflow when a new comment is posted on an existing issue?

* [ ] A.	discussion_comment
* [ ] B.	issue_comment
* [ ] C.	issues
* [ ] D.	issues.comment

=== Question 41

In a GitHub Actions job that uses a matrix with the keys runtime and os, how do you reference the selected values within a step?

* [ ] A.	Use vars.runtime and vars.os
* [ ] B.	Use the matrix context like matrix.runtime and matrix.os
* [ ] C.	Use env.runtime and env.os

=== Question 42

In GitHub Actions when an environment requires reviewers, what happens to a deployment job that has been waiting for approval for 90 days?

* [ ] A.	Remains waiting indefinitely
* [ ] B.	Marked as failed after 90 days without approval
* [ ] C.	Canceled after the approval window

=== Question 43

What should you do to prevent a GitHub Actions workflow from running until an external API is healthy again?

* [ ] A.	Delete the workflow file from the repository
* [ ] B.	Set continue-on-error on the API call step
* [ ] C.	Disable the workflow so it does not run until the API is healthy again
* [ ] D.	Edit the workflow to skip the API step until the service is back online

=== Question 44

In a GitHub Actions workflow badge URL, which query parameter displays the status of a specific branch?

* [ ] A.	?event=push
* [ ] B.	?branch=release-25-03
* [ ] C.	?ref=main

=== Question 45

A JavaScript GitHub Action intermittently fails within the first 60 seconds on a hosted runner. What is the quickest initial step to determine what failed and why?

* [ ] A.	Switch the JavaScript action to a Docker container action
* [ ] B.	Enable step debug logs with ACTIONS_STEP_DEBUG
* [ ] C.	Open the workflow run and read the failed step logs for errors

=== Question 46

When selecting the operating system for a GitHub Actions runner to execute workflows, which factor should primarily guide the choice?

* [ ] A.	Team OS familiarity
* [ ] B.	OS compatibility with required tooling and dependencies
* [ ] C.	Workflow minutes cost

=== Question 47

In a GitHub Actions job log, what information is shown in the "Set up job" section? (Choose 3)

* [ ] A.	Repository secrets list
* [ ] B.	GITHUB_TOKEN permissions
* [ ] C.	Runner image
* [ ] D.	Code scanning results
* [ ] E.	Operating system

=== Question 48

How should a maintainer describe and categorize a GitHub Action in the GitHub Marketplace to maximize discoverability and clarity?

* [ ] A.	Add many unrelated topics and keywords to broaden reach
* [ ] B.	Provide a long feature list to attract many teams
* [ ] C.	Use a clear and concise description and choose one most relevant category

=== Question 49

What is the minimum supported cron schedule interval for GitHub Actions workflows?

* [ ] A.	Every fifteen minutes
* [ ] B.	Five minute interval
* [ ] C.	Every one minute

=== Question 50

In a single GitHub Actions step, what happens when the "continue-on-error" key is set and the step fails?

* [ ] A.	It forces the step to run every time regardless of earlier failures or conditions
* [ ] B.	It lets the workflow proceed even when that step fails
* [ ] C.	It sets the job-level continue-on-error so the whole job can fail without failing the workflow
* [ ] D.	It disables fail fast behavior for matrix jobs so parallel runs are not cancelled

=== Question 51

Before submitting a GitHub Action to the GitHub Marketplace, which repository requirement must be met?

* [ ] A.	Enable GitHub Pages for the repository
* [ ] B.	Host the action in a private repository
* [ ] C.	Keep the action metadata file at the repository root
* [ ] D.	Place the action metadata file inside an actions subdirectory

=== Question 52

How can you limit repository access to specific self-hosted runner pools while maintaining isolation between departments?

* [ ] A.	Add labels to self-hosted runners and reference those labels in runs-on
* [ ] B.	Create runner groups with repository access controls
* [ ] C.	Required workflows
* [ ] D.	GitHub Environments with required reviewers

=== Question 53

When a GitHub Actions job specifies multiple custom labels in the runs on field, how must a self-hosted runner's labels match for the job to be assigned to it?

* [ ] A.	Runner groups decide routing not labels
* [ ] B.	Labels are auto assigned from OS and hardware
* [ ] C.	Any one matching label is enough
* [ ] D.	Runner must include every listed label

=== Question 54

In GitHub Actions workflows, how should you reference third party actions to keep pipelines stable while adopting updates safely?

* [ ] A.	Use the latest tag
* [ ] B.	Use the action&apos;s default branch
* [ ] C.	Pin to a major version then refine to a minor tag or commit when needed
* [ ] D.	Use the newest commit SHA

=== Question 55

When a push trigger specifies both branch and path filters, under what condition does the workflow run?

* [ ] A.	Filters are evaluated in order and the first match triggers
* [ ] B.	It runs when either the branch pattern or the path pattern matches
* [ ] C.	It runs only when both branch and path filters match
* [ ] D.	Path filters apply only to pull requests so push uses only branches

=== Question 56

Which statements accurately describe the practical differences between GitHub hosted runners and self hosted runners in GitHub Actions? (Choose 3)

* [ ] A.	Self hosted runners often persist and retain tools and caches between jobs
* [ ] B.	GitHub hosted runners have default access to private VPC resources
* [ ] C.	GitHub hosted runners use a fresh virtual machine for every job so runs start clean
* [ ] D.	Self hosted runners can reach internal networks while GitHub hosted runners cannot by default

=== Question 57

In GitHub Actions caching, what is the purpose of the restore-keys setting when the primary cache key is not found?

* [ ] A.	Allow cross-OS cache reuse
* [ ] B.	Provide fallback key prefixes tried in order
* [ ] C.	Set fail-on-cache-miss behavior

=== Question 58

In a GitHub Actions workflow that runs a Docker container action, the entrypoint.sh script fails with a permission denied error. What is the simplest change to ensure the script runs?

* [ ] A.	Use a composite action instead of a Docker action
* [ ] B.	Run chmod +x on entrypoint.sh before the container action runs
* [ ] C.	Switch to a different entry point script

=== Question 59

When repository settings are left at their defaults, how long are GitHub Actions workflow run logs and artifacts retained?

* [ ] A.	1 year
* [ ] B.	90 days
* [ ] C.	Indefinitely
* [ ] D.	30 days

=== Question 60

In a GitHub Actions job running on an Ubuntu runner, how can you add /opt/cli to the PATH so it is available in all subsequent steps?

* [ ] A.	Set PATH in a job-level env
* [ ] B.	Echo &quot;/opt/cli&quot; to $GITHUB_PATH in a run step
* [ ] C.	Append &quot;/opt/cli&quot; to $GITHUB_STEP_SUMMARY in a run step
* [ ] D.	Append &quot;/opt/cli&quot; to $GITHUB_ENV in a run step

=== Question 61

How can a team prevent containerized self-hosted ephemeral runners from updating while jobs are running and maintain control over when the runner image is upgraded?

* [ ] A.	GitHub-hosted runners
* [ ] B.	Disable runner self update and pin the runner version in the container image
* [ ] C.	Enable automatic runner updates

=== Question 62

In the GitHub Actions run interface, how can you share a direct link to a specific line in the step log?

* [ ] A.	Download the logs and email the file
* [ ] B.	Create a permalink from the line number in the step log
* [ ] C.	Grant write access so the run logs can be opened
* [ ] D.	Share a GitHub Gist of the line

=== Question 63

In GitHub Actions workflows, which YAML rules govern indentation and line breaks?

* [ ] A.	Tabs and spaces can be mixed if indentation levels stay consistent
* [ ] B.	GitHub Actions workflows use JSON so line breaks are insignificant
* [ ] C.	YAML is whitespace sensitive and forbids tab indentation and it is a superset of JSON

=== Question 64

In GitHub Actions, what is the primary purpose of committing pinned dependencies only on release tags and triggering builds only during the release event?

* [ ] A.	Run builds on all branches
* [ ] B.	Improve supply chain security by pinning at tag and building on release
* [ ] C.	Discourage use of tags or SHAs by consumers
* [ ] D.	Commit lockfiles to the main branch for faster feedback

=== Question 65

When should you use a hybrid of GitHub hosted runners and self hosted runners to optimize cost and developer feedback time?

* [ ] A.	Use only GitHub Actions larger runners for all jobs
* [ ] B.	Use a hybrid when workloads mix quick checks with compute heavy builds and you want balanced cost and speed
* [ ] C.	Use a hybrid when every job must be isolated and security overrides performance and cost

<<<

== No Fluff, Just Stuff Practice Exam Answers

=== Question 1

****

In GitHub Actions, how is the success or failure of a step determined by its exit code?

* [*] B.	Zero exit code means success and any nonzero means failure

****

The correct option is *Zero exit code means success and any nonzero means failure*.

GitHub Actions evaluates each step by the exit status of the process it runs. The runner marks a step successful when the command finishes with an exit status of 0. If the command returns any other code then the step is marked as failed and the job may stop depending on your workflow configuration.

_Exit codes are ignored and a maintainer sets the result manually_ is incorrect because the runner automatically determines success or failure from the process exit status and does not require manual intervention for step outcomes.

_Success is controlled by continue-on-error rather than the exit code_ is incorrect because continue-on-error only influences whether a failing step stops the job. The step is still classified as failed or successful based on its exit status.

_Every exit code is a failure_ is incorrect because an exit status of 0 indicates success by design.

=== Exam Tip

When you see options about step outcomes, anchor your reasoning to the standard convention that _0_ means success and any _nonzero_ value means failure. Distinguish this from features like _continue-on-error_ that affect whether the workflow proceeds rather than how success or failure is determined.

=== Question 2

****

Which configuration lines correctly set the workflow name in a GitHub Actions workflow file? (Choose 2)

* [*] B.	name: $ &apos;release-flow-42&apos; 
* [*] D.	name: release-flow-42

****

The correct options are *name: release-flow-42* and *name: $ 'release-flow-42' *. Both set the workflow name that appears in the Actions interface and on the workflow page.

The plain static name key with a simple string sets the workflow name clearly and predictably. It is the most straightforward way to define the workflow title.

The expression form with a single quoted string evaluates to the same literal value. GitHub Actions accepts a string result for the workflow name, so this produces a valid name while keeping consistency with other places where expressions are used.

_name: $ "release-flow-42" _ is not valid as written in this context because the inner double quotes can cause parsing issues and do not produce a clean string literal for the workflow name in this exam scenario.

_run-name: release-flow-42_ does not set the workflow name. It only sets the display name for each workflow run, so it does not answer the question that asks for the workflow name.

=== Exam Tip

Confirm whether the question targets the _workflow name_ or the _run name_. The top level _name_ sets the workflow title while _run-name_ only changes the title of each run.

=== Question 3

****

In GitHub Enterprise Cloud, where do you set the policy that allows only enterprise hosted actions and reusable workflows to run?

* [*] B.	Enterprise account Actions policy

****

The correct option is *Enterprise account Actions policy*.

The *enterprise Actions policy* is the centralized place where enterprise owners enforce which actions and reusable workflows are permitted across all organizations in GitHub Enterprise Cloud. From this scope you can require that only actions and reusable workflows hosted within the enterprise are allowed to run, and this policy flows down to organizations and repositories to ensure consistent enforcement.

_Organization settings Policies then Actions_ is not correct because organization level policies apply only within a single organization and cannot guarantee enterprise wide enforcement. The requirement to limit runs to enterprise hosted actions and reusable workflows must be set at the enterprise scope.

_Repository settings Actions general_ is not correct because repository settings control repository specific behavior such as enabling Actions or setting permissions. They do not provide an enterprise wide control for allowing only enterprise hosted actions and reusable workflows.

=== Exam Tip

Look for the scope hinted by the question. If it says _enterprise wide_ or applies to all organizations then choose enterprise account settings. If it mentions a single _organization_ or _repository_ then select the corresponding scope.

=== Question 4

****

In GitHub Actions, where should you declare custom environment variables so they are accessible across all jobs and steps in a single workflow run?

* [*] B.	Set env in the workflow YAML

****

The correct option is *Set env in the workflow YAML* because defining environment variables at the top level of a workflow makes them available to every job and step in that single run.

In a workflow file you can declare a top level mapping for environment variables with key value pairs. This top level scope propagates the values to all jobs and steps in the run and you can override them at job or step scope when necessary. This is the most direct way to share non secret configuration across the entire workflow execution.

_Repository variables_ are not defined in the workflow and are scoped to the repository rather than a single run. These values live in settings and must be referenced through the vars context which means they are not automatically available as environment variables in every job and step.

_Environment secrets_ are intended for sensitive data and are tied to a deployment environment. Secrets do not become plain environment variables unless you explicitly map them and they are not meant for general non sensitive configuration.

_Runner command line arguments_ do not provide a way to set per run environment variables for GitHub Actions. The runner does not accept a command line flag that injects variables across jobs and steps in a workflow.

=== Exam Tip

When a question stresses availability across jobs and steps within one run, think of the _workflow level env_. If the scenario involves sensitive values choose _secrets_. If it asks for reuse across many workflows look for _repository variables_.

=== Question 5

****

Which GitHub Actions event configuration triggers only for pull requests targeting the release branch and not for push events?

* [*] B.	on: pull_request: branches: - release

****

The correct option is *on: pull_request: branches: - release*. This configuration runs only when a pull request targets the release branch and it does not run on push events.

The pull_request event triggers on pull request activity and the branches filter matches the base branch of the pull request. By specifying the release branch, this configuration limits runs to pull requests that target that branch. Because it listens only for the pull_request event, pushes will not trigger the workflow.

_on: pull_request_target: branches: - release_ listens for pull request activity but it runs in the context of the target repository with different permissions and is intended for special cases. The question asks for the standard pull request trigger, so this is not the best match.

_on: push: branches: - release_ is incorrect because it triggers on pushes to the release branch and the question requires that it not run on push events.

_on: pull_request: types: - opened_ is incorrect because it does not filter by the base branch. It would run for any pull request that is opened regardless of the target branch and it would miss other common pull request activities such as synchronize or reopened.

=== Exam Tip

When a scenario calls for branch specific pull request triggers, prefer the _pull_request_ event with a _branches_ filter and verify that no _push_ trigger is present.

=== Question 6

****

In GitHub Actions, which workflow key defines the events that trigger the workflow such as push or pull_request?

* [*] B.	on:

****

The correct option is *on:* which specifies the events such as push and pull_request that trigger a GitHub Actions workflow to run.

In a workflow file this key accepts one or many events and can include filters like branches and paths for push and pull_request so it defines exactly when the workflow starts.

The option _if:_ controls conditional execution of jobs or steps and it does not configure which events start a workflow.

The option _env:_ sets environment variables at the workflow job or step level and it does not declare triggers.

The option _jobs:_ defines the jobs and their steps within a workflow and not the events that trigger it.

=== Exam Tip

When a question asks about triggers look for the key that maps to _events_ at the top of the workflow file and rule out keys that handle _conditions_ or _variables_ or define _jobs_.

=== Question 7

****

What repository visibility is required for a GitHub Action to be listed on GitHub Marketplace?

* [*] C.	Public repository

****

The correct option is *Public repository*.

GitHub only lists actions from repositories that are visible to everyone. This is a firm requirement for publishing an action to the Marketplace and private or internal repositories cannot be listed.

_Verified creator status_ is not required to list an action. Verification only grants a trust badge for an organization and you can publish without it.

_Metadata in a subfolder_ is incorrect because GitHub requires the action metadata file to be in the root of the repository. Placing the metadata file in a subfolder does not meet this requirement.

_Use GitHub Container Registry_ is not required for Marketplace listing. Container actions can use other registries or be built from a Dockerfile and Marketplace does not mandate GHCR.

=== Exam Tip

When you see Marketplace listing questions, identify the must have repository setting. The repository must be _public_ while badges and specific packaging choices are often _optional_.

=== Question 8

****

Which GitHub Actions capability prevents secrets from appearing in workflow logs?

* [*] C.	Default secret masking in logs

****

The correct option is *Default secret masking in logs*.

GitHub Actions automatically redacts secret values from workflow logs so if a command prints a secret the value is masked in the output. This built in protection helps prevent accidental exposure of credentials during job execution and it applies without additional configuration.

_Manual approval for secret log output_ is not a GitHub Actions feature for hiding secrets in logs. Manual approvals are used for protected environments and deployments rather than controlling log redaction.

_GitHub Audit Log_ records administrative and security relevant events. It does not mask or govern what appears in workflow logs.

_Encrypted secrets written to logs_ is not a safety feature. You should avoid writing secrets to logs in any form and GitHub relies on automatic masking of secret values rather than encouraging encrypted output in logs.

=== Exam Tip

Scan options for _default_ or _automatic_ protections when the question asks how something is prevented. For GitHub Actions logs the keyword to spot is _masking_ rather than auditing or approvals.

=== Question 9

****

In a workflow triggered by a pull request comment, which GitHub Actions context property contains the event payload used to access the comment text and the pull request number?

* [*] B.	github.event

****

The correct option is *github.event*.

In a workflow that runs on a pull request comment the event context contains the webhook payload. With *github.event* you can read the structured fields for the comment text and the pull request number. The comment text is available under the comment body field and the pull request number is available under the issue number for comment events or under the pull request number for pull request events. This makes *github.event* the direct and convenient source for these values.

The option _github.repository_ only provides the owner and repository name. It does not expose the event payload so it cannot give you the comment text or the pull request number.

The option _github.event_path_ points to a temporary file on the runner that contains the JSON payload. It does not provide the data directly in the context and using *github.event* is the recommended way to access the payload fields in expressions and steps.

The option _github.job_ identifies the current job in the workflow run. It does not include any event payload so it cannot be used to read the comment or the pull request number.

=== Exam Tip

When a question asks where to read details from a GitHub Actions trigger look for the context that holds the _webhook payload_ and verify the exact _field names_ you need such as comment body and issue number.

=== Question 10

****

Which repository files are required for a Docker container action and for a JavaScript action to run correctly? (Choose 3)

* [*] A.	JavaScript entry file such as main.js or index.js
* [*] C.	Action metadata file action.yml or action.yaml
* [*] D.	Container action Dockerfile

****

The correct options are *JavaScript entry file such as main.js or index.js*, *Action metadata file action.yml or action.yaml*, and *Container action Dockerfile*.

The *Action metadata file action.yml or action.yaml* is mandatory because it declares inputs and outputs and it instructs GitHub how to run the action. Both JavaScript and container actions rely on this metadata to execute correctly.

For a JavaScript action the *JavaScript entry file such as main.js or index.js* is the script that the runner executes as directed by the metadata. GitHub expects a committed distributable script, so the entry file must be present in the repository.

For a container action the *Container action Dockerfile* defines how to build the image and what command to run, which makes the *Dockerfile* required for the action to work.

The option _package.json_ is not required for a working action. It can be useful during development and for dependency management, yet a JavaScript action can run from the bundled output without _package.json_ and a container action does not need _package.json_ at runtime.

=== Exam Tip

Map file requirements to the action type. Remember that the _metadata file_ is always required and that the _entry file_ or _Dockerfile_ is needed based on whether it is a JavaScript or container action. Treat _package.json_ as helpful for development rather than required at runtime.

=== Question 11

****

Which type of GitHub Actions runner gives you full control over the execution environment for proprietary tools and supports elastic scaling?

* [*] B.	Self hosted runners on virtual machines you manage

****

The correct option is *Self hosted runners on virtual machines you manage*.

With this choice you control the operating system, networking, and the entire software stack. You can install proprietary and licensed tools and keep them private. You can also achieve elasticity by programmatically creating more virtual machines, registering them as runners during peak demand, and removing them when demand falls.

_GitHub hosted runners_ are convenient and maintained by GitHub, yet you do not control the base image or the underlying host and you cannot run privileged or specialized proprietary software that requires full administrative control.

_GitHub Actions larger runners_ provide more CPU, memory, and storage, but they are still fully managed by GitHub and do not grant full control of the environment, so they do not satisfy strict proprietary tooling or custom image requirements.

_GitHub Codespaces_ is a cloud development environment for coding and debugging, not a GitHub Actions runner, so it does not meet the requirement to run workflows with full control or elastic scaling of runners.

=== Exam Tip

When you see a requirement for _full control_ of the environment and the need to run _proprietary_ tools, map that to self hosted runners. Then confirm whether the scenario also needs _elastic scaling_ and think about how you would add or remove runners programmatically.

=== Question 12

****

In GitHub Actions, what is the correct relationship among events, workflows, jobs, steps, and actions?

* [*] C.	An event triggers a workflow that runs one or more jobs and each job has steps that use actions

****

The correct statement is *An event triggers a workflow that runs one or more jobs and each job has steps that use actions*.

In GitHub Actions an event such as push or pull_request starts a workflow. The workflow defines one or more jobs that usually run on separate runners and can run in parallel. Each job is made of steps that execute shell commands or call reusable actions. Actions are invoked by steps rather than by workflows directly.

_A repository_dispatch starts the pipeline and the workflow runs actions directly without jobs or steps_ is wrong because although repository_dispatch is a valid event, workflows always contain jobs and jobs contain steps, and actions are used within steps rather than being run by workflows directly.

_Jobs hold one or more actions and workflows are collections of steps across jobs_ is wrong because jobs hold steps and steps use actions, and a workflow is a collection of jobs rather than steps.

_Steps start actions and actions start workflows that run jobs_ is wrong because steps can invoke actions, but actions do not start workflows. Only events trigger workflows.

=== Exam Tip

Map the chain in order and check that nothing is skipped. Think _event_ then _workflow_ then _jobs_ then _steps_ then _actions_. If an option jumps over jobs or steps or lets actions trigger workflows it is likely incorrect.

=== Question 13

****

In a custom GitHub Action, which metadata key is used to expose values to subsequent workflow steps?

* [*] B.	outputs

****

The correct option is *outputs*.

This key is defined in an action metadata file and it exposes named values that the action sets so later steps in the workflow can read them. It provides a supported way for an action to pass computed information forward to subsequent steps.

_runs_ is not correct because it only defines how the action executes and what runtime or strategy it uses and it does not expose values to later steps.

_branding_ is not correct because it only affects the icon and color shown in the GitHub Marketplace and it has no effect on data flow in workflows.

_inputs_ is not correct because it declares parameters that users pass into the action and it does not make values available after the action finishes.

=== Exam Tip

When the question asks about passing data from an action to later steps, map the direction. _inputs_ go into an action and _outputs_ come out, while _runs_ and _branding_ only describe execution and appearance.

=== Question 14

****

In GitHub Actions, why is it better for workflows to reference file paths using variables rather than hardcoded paths when running on hosted and self hosted runners?

* [*] B.	Variables let workflows adapt to different runner paths

****

The correct option is *Variables let workflows adapt to different runner paths*. This keeps workflows portable across GitHub hosted and self hosted runners.

This is correct because runner directory layouts differ by operating system and by whether the machine is GitHub hosted or self hosted. A workflow that uses environment variables and contexts for paths resolves to the correct location on each runner at runtime. Using values like GITHUB_WORKSPACE or runner.temp avoids brittle assumptions and prevents failures when the workspace or temporary directories differ between machines.

_GitHub Actions blocks hardcoded paths_ is incorrect because the service does not block them. You can write fixed paths, although they are fragile and often break when the job runs on a different operating system or a differently configured self hosted runner.

_GITHUB_WORKSPACE is the same on all runners so fixed paths are safe_ is incorrect because while the variable name is consistent, the actual filesystem path it resolves to varies across operating systems and runner configurations. Relying on a literal path is therefore not portable.

=== Exam Tip

When you see path portability questions, think in terms of _environment variables and contexts_ and imagine the job running on Linux, Windows, and macOS as well as on a custom self hosted machine.

=== Question 15

****

What is the best way to publish a reusable GitHub Action that accepts multiple inputs to ensure wide discoverability and a clear contract for consumers?

* [*] B.	Public repository with action metadata and Marketplace listing

****

The correct option is *Public repository with action metadata and Marketplace listing*.

A *public repository with action metadata* gives your action a clear and machine readable contract. The action.yml or action.yaml file defines inputs, outputs, defaults and validation which lets consumers know exactly how to use the action and lets GitHub validate workflow usage. Pairing this with a *Marketplace listing* makes the action easy to find through search and categories and it encourages proper release tagging so users can pin reliable versions.

_Publish only to GitHub Container Registry_ is insufficient because a container registry stores images but it does not define the action interface and it does not make the action easily discoverable. Even for Docker based actions you still need a repository with an action metadata file and a *Marketplace listing* for broad discovery and a clear contract.

_Public repo and README only_ does not provide a formal interface since a README is not parsed by GitHub for inputs or outputs and it does not validate workflow usage. Without action metadata and a *Marketplace listing* the action is harder to discover and lacks a reliable contract for consumers.

=== Exam Tip

When you see the words _discoverable_ and _clear contract_ think in terms of a public repo with an _action.yml_ that defines inputs and outputs and a _Marketplace_ listing for search and adoption.

=== Question 16

****

In the Actions view, which filter displays only runs that were triggered by pull request events?

* [*] C.	Event

****

The correct option is *Event*.

In the Actions view, the *Event* filter lets you narrow runs by the GitHub event that triggered them. If you choose the pull_request event then the list will show only runs that were started by pull request activity.

_Branch_ is incorrect because it filters runs by the source or target branch name and not by the triggering event, so it cannot isolate pull request triggered runs across all branches.

_Workflow_ is incorrect because it filters by the specific workflow file or workflow name and not by the event that triggered the runs.

=== Exam Tip

Look for wording that says runs are _triggered_ by something. That usually points to the _Event_ filter rather than filters that target branches or specific workflow files.

=== Question 17

****

Under what circumstances should a team choose GitHub hosted runners to minimize maintenance and enable rapid onboarding?

* [*] B.	when they want GitHub to provide ephemeral runners that scale automatically with no setup

****

The correct option is *when they want GitHub to provide ephemeral runners that scale automatically with no setup*. This aligns with *GitHub-hosted runners* which are fully managed by GitHub so they start quickly and require no infrastructure work from the team.

With *GitHub-hosted runners* the platform automatically scales to meet concurrent job demand and each job runs in a fresh ephemeral environment with common toolchains preinstalled. Teams avoid building and patching images which keeps maintenance low and makes onboarding fast.

_when they need job traffic to come from fixed IP addresses for firewall allowlists_ is not a fit for *GitHub-hosted runners* because their egress comes from shared address ranges that can change over time. If a single static egress address must be allowlisted then a self-hosted runner or routing through a stable corporate egress is the right approach.

_when they require root access and complete control of the runner environment for compliance_ points to self-hosted runners. *GitHub-hosted runners* offer limited control of the underlying virtual machine and changes do not persist across jobs which does not meet strict control requirements.

=== Exam Tip

Scan for phrases that signal a managed service such as _ephemeral_, _auto scaling_, and _no setup_. Needs like _fixed IPs_ or _full control_ usually indicate self-hosted runners instead.

=== Question 18

****

In GitHub Actions, which feature allows you to target specific self-hosted runners for jobs without naming individual runners?

* [*] B.	runner labels

****

The correct option is *runner labels* because they allow you to target a class of self hosted runners by shared labels so you do not need to identify any single machine.

This feature works by assigning one or more labels to each self hosted runner so that the job configuration can request a label and GitHub will match any available runner that has it. This approach scales well as you can add or remove machines without changing workflow files and it keeps selection based on capabilities rather than specific hosts.

_environments_ focus on deployment rules, approvals, and secrets management and they do not control which specific runners execute a job through the job runner specification.

_matrix strategy_ creates multiple job variants from a set of parameters and it does not determine which machines are selected to run those jobs.

_runner groups_ are used to organize and scope access to self hosted runners for repositories or organizations and they do not select runners for an individual job which is done through labels.

=== Exam Tip

When a question hints at targeting groups of self hosted machines without naming hosts, think about _labels_. If the wording emphasizes access control, that points to _groups_, and if it emphasizes approvals or secrets, that points to _environments_.

=== Question 19

****

In a GitHub Actions step that runs shell commands, which command writes a debug message to the job log?

* [*] B.	echo &quot;::debug::start bootstrap script&quot;

****

The correct option is *echo "::debug::start bootstrap script"*. This uses the GitHub Actions workflow command for debug messages so it writes a debug entry to the job log.

GitHub Actions interprets special workflow commands that are printed to standard output. When the command uses the debug token it marks the line as a debug message that the runner records in the log. These messages are only visible when step debug logging is enabled. Using echo is the usual way to emit the command from a shell step.

_echo "::notice::start bootstrap script"_ writes a notice level annotation rather than a debug message so it does not produce a debug entry.

_set -x_ enables shell tracing inside the current process and prints executed commands but it is not a GitHub Actions workflow logging command so it does not write a debug message.

_Set ACTIONS_STEP_DEBUG to true in repository secrets_ controls whether debug messages are shown in logs but it does not write a message from a shell step so it is configuration rather than the requested command.

=== Exam Tip

Match the requested log level to the workflow command token and remember that _::debug::_ writes debug messages while visibility may require that step debug logging is enabled.

=== Question 20

****

Within a GitHub repository, where are the GitHub Actions workflow YAML files stored?

* [*] B.	the .github/workflows directory

****

The correct option is *the .github/workflows directory*.

GitHub Actions discovers and runs workflow files only when they are saved in this path within the repository. Each workflow is a YAML file with a .yml or .yaml extension and GitHub reads these files to determine events, jobs, and steps to execute.

The option _the Actions tab in the repository_ is incorrect because that tab is a user interface for viewing runs and managing workflows. It is not a place where files are stored in the repository.

The option _the .github/actions directory_ is incorrect because that directory is intended for custom actions that your repository defines and includes the action metadata and implementation. It is not used for workflow files.

=== Exam Tip

Map concepts to paths by remembering that _workflows_ live in _.github/workflows_ and _custom actions_ live in _.github/actions_. The Actions tab is only a user interface view.

=== Question 21

****

In a GitHub Actions status badge URL, how can you limit the badge to show only workflow runs triggered by the push event?

* [*] B.	Add ?event=push to the badge URL

****

The correct option is *Add ?event=push to the badge URL*.

Adding the event query parameter with the value push filters the status badge to display only runs that were triggered by the push event. This change affects only the badge output and does not modify the workflow configuration. You can also pair this with the branch parameter if you need to show results for a specific branch.

_GitHub Pages_ is unrelated because it is a static site hosting feature and it does not control how an Actions badge is filtered by event.

_Use the branch name as the event parameter in the badge URL_ is incorrect because the event parameter expects an event type such as push. Branch selection is done with the branch parameter and not through the event parameter.

_Change the on section of the workflow file to only include the push trigger_ would restrict when the workflow runs, yet it does not address filtering the existing badge using its URL. The question asks for a badge URL change rather than a workflow configuration change.

=== Exam Tip

When a question asks about filtering a badge, look for URL query parameters such as _event_ and _branch_. If the filter is about triggers, choose _event=push_ rather than changing the workflow file.

=== Question 22

****

Which naming strategy for shared GitHub Actions components across repositories best supports discovery, reuse, and versioning?

* [*] C.	Adopt and enforce a unified naming convention that encodes component type purpose and version

****

The correct option is *Adopt and enforce a unified naming convention that encodes component type purpose and version*.

This strategy creates predictable names that encode type, purpose, and version, which improves searchability and discovery across repositories. It supports consistent reuse and enables clear version pinning in workflow references like owner or repo or path at v1. It reduces ambiguity when teams consume composite actions and reusable workflows and it makes automation for cataloging and auditing easier. It also aligns with GitHub guidance to version actions and to use clear metadata so components are understandable and maintainable.

_Rely on repository topics and code search for discovery instead of standardizing names_ is incorrect because ad hoc search and topics are inconsistent, hard to scale, and do not guarantee that components are named in a way that communicates type and version, which hurts reliable discovery and reuse.

_Use repository releases and tags for versioning but skip naming conventions_ is incorrect because tags alone do not solve findability across repositories. Without a consistent naming pattern, teams struggle to locate the right component and to understand its purpose and scope even if versions exist.

_Allow each product team to define its own naming pattern for reusable components_ is incorrect because divergent patterns fragment the ecosystem, reduce cross team discoverability, and make automated cataloging or governance difficult. It also increases confusion and duplication of effort.

=== Exam Tip

When a question ties _discovery_, _reuse_, and _versioning_ together, favor answers that emphasize _consistent naming_ plus version pinning. Avoid options that rely only on search or that allow every team to choose its own pattern.

=== Question 23

****

To maximize discoverability and adoption by external maintainers, where should you publish a reusable GitHub Action?

* [*] B.	GitHub Marketplace

****

The correct option is *GitHub Marketplace* as it is the primary place where developers look for reusable GitHub Actions and it provides the best path to discovery and adoption.

Publishing your action in *GitHub Marketplace* makes it discoverable through search, categories, and curated lists. The listing can present documentation, version information, permissions, and usage examples, and users can easily add the action to workflows which improves adoption.

_GitHub Packages_ is for hosting and distributing packages such as container images or libraries. While an action can reference a container image stored in _GitHub Packages_, it is not where users browse and find actions and it does not provide the dedicated listing and discovery features that the *GitHub Marketplace* offers.

_A public GitHub repository_ is necessary to share an action openly, yet it does not maximize discoverability on its own. Without a listing in the *GitHub Marketplace*, the action relies on organic search or direct links which typically results in lower adoption.

=== Exam Tip

When a question emphasizes _discoverability_ or _adoption_ think of the central _catalog_ that developers browse and choose the Marketplace, while questions about where the code lives point to a repository or a registry.

=== Question 24

****

In a GitHub Actions workflow for integration tests that depend on PostgreSQL and Redis, what is the primary advantage of using service containers?

* [*] B.	Run dependent services as ephemeral containers in the job

****

The correct option is *Run dependent services as ephemeral containers in the job*.

This approach lets your workflow start PostgreSQL and Redis on demand inside the same network as the job and they are removed when the job completes. It gives you a realistic and isolated environment for integration tests without managing external infrastructure and it keeps each run clean and repeatable.

_Dependency caching with actions/cache_ is about saving and restoring files to speed up later runs. It does not provide running databases or message stores for tests.

_Faster code compilation during build steps_ is not the primary benefit of service containers. Starting PostgreSQL or Redis as services does not make compilation faster.

_Automatic code vulnerability detection during the pipeline_ refers to security scanning features. Service containers do not perform code analysis or vulnerability detection.

=== Exam Tip

When you see databases like PostgreSQL or Redis for _integration tests_ in a workflow question, look for answers that mention _service containers_ that run with the _job_. Distractors often focus on _caching_ or _security scanning_ which are different concerns.

=== Question 25

****

To help other teams quickly adopt a reusable GitHub Action, what is the first piece of documentation you should create?

* [*] B.	Create a clear README with description, inputs, outputs, secrets, and examples

****

The correct option is *Create a clear README with description, inputs, outputs, secrets, and examples*.

This gives teams a single source of truth that shows what the action does and how to use it. It quickly answers the questions they have such as what parameters are required, what secrets must be provided, what outputs are produced, and how to wire it into a workflow. Including copy paste usage examples reduces adoption friction and allows teams to validate the action in minutes.

Capturing inputs and outputs in the repository documentation also complements the action metadata so users do not have to inspect action.yml. Clear setup notes and permission expectations prevent misconfiguration and speed reviews.

The option _Publish to GitHub Marketplace_ is not the first step because a listing without strong documentation will not help teams adopt the action quickly. Publishing typically comes after you have a stable version and a complete README so that the marketplace page can present everything users need.

The option _Build an interactive setup walkthrough_ can be helpful for complex products but it is not necessary for a reusable action. Teams primarily need concise usage examples and parameter details which are faster to produce and easier to maintain in a README.

The option _Compile a full feature catalog_ focuses on marketing rather than practical adoption. Teams care first about how to call the action, what it requires, and what it returns which is best delivered through clear usage documentation.

=== Exam Tip

When you see a question about what to do _first_ choose the smallest deliverable that unblocks users quickly. A concise _README_ with inputs outputs examples and secrets usually precedes publishing or advanced tooling.

=== Question 26

****

In GitHub Actions, what is the main purpose of workflow commands issued within a run step?

* [*] C.	Send directives and metadata to the runner

****

The correct option is *Send directives and metadata to the runner*. Workflow commands are special messages emitted during a run step that the GitHub Actions runner interprets to adjust behavior, pass data, and control logging.

These commands let the runner do things like set outputs for later use, mask sensitive values in logs, group or ungroup log sections, and write data to the environment files that persist for subsequent steps in the same job. They communicate intent to the runner rather than execute business logic.

The option _Run custom scripts on the runner_ is incorrect because a run step already executes scripts and shell commands. Workflow commands do not run your code and instead they instruct the runner about how to handle metadata and runtime behavior.

The option _Set environment variables for the whole workflow_ is incorrect because commands can set variables that persist for later steps in the same job and can pass values between jobs using outputs. They do not automatically create global variables that apply to every job across the entire workflow.

The option _Trigger another workflow_ is incorrect because commands do not start workflows. Workflows start in response to events or manual and API triggers rather than through workflow command messages.

=== Exam Tip

Identify when the question is about _communicating with the runner_ rather than executing code. If the action is about _metadata_, _outputs_, or _log control_, it points to workflow commands rather than scripts or triggers.

=== Question 27

****

What is the best way to structure reusable GitHub Actions workflows to provide consistent CI across more than 60 repositories while ensuring they are versioned and easy to maintain?

* [*] C.	Central repository workflows invoked with workflow_call and version tags

****

The correct option is *Central repository workflows invoked with workflow_call and version tags*.

This approach lets you keep a single set of reusable workflow files that other repositories can call directly. You expose the workflows with the workflow_call trigger and consumers reference them by repository and path with a stable tag or a commit SHA. Teams can pin to a version for stability while you evolve the central definitions and publish new tags. This delivers consistency across many repositories and keeps maintenance focused in one place.

You can ship changes by updating a minor or patch tag and let repositories adopt them on their schedule. For larger breaking changes you release a new major tag and consumers can opt in. Inputs and secrets can be defined once and enforced uniformly which improves reliability and governance.

_Starter Workflows in the .github repository_ is not correct because these are templates that get copied into each repository. After copying they are no longer centrally managed so updates require manual edits in every repository and you cannot guarantee consistent behavior over time.

_Use branches and tags for workflows in each repository_ is not correct because duplicating workflow logic across many repositories creates drift and high maintenance. Local branches or tags do not provide shared reuse or callable workflows and you would still need to touch every repository to make changes.

=== Exam Tip

Look for keywords that imply true reuse and controlled _versioning_. Mentions of _workflow_call_ with tags or SHAs usually point to the best scalable design for many repositories.

=== Question 28

****

In GitHub Actions, how can you configure a workflow to run only on weekdays Monday through Friday?

* [*] B.	Use a cron expression in the schedule event that matches weekdays only

****

The correct option is *Use a cron expression in the schedule event that matches weekdays only*.

This works because GitHub Actions supports the schedule event which uses POSIX cron syntax. You can restrict runs to Monday through Friday by setting the day of week field to one through five. The scheduler interprets times in Coordinated Universal Time, so choose the hour and minute with that in mind, and the workflow will only run on weekdays.

_Add a job level if that checks the weekday and skips Saturday and Sunday_ is not correct because it does not control when the workflow is scheduled. The workflow would still be triggered on weekends and the job would only be skipped at runtime which is inefficient and does not truly schedule weekdays only.

_Invoke workflow_dispatch on weekdays using Azure Logic Apps_ is not correct because it relies on an external service and uses a manual or API trigger rather than the built in scheduler. GitHub Actions already provides native scheduling so this approach adds unnecessary complexity.

=== Exam Tip

When a question asks about time based automation in GitHub Actions, look for the _schedule_ trigger with a _cron_ expression and remember that execution times are _UTC_ and weekdays are represented by _one through five_ in the day of week field.

=== Question 29

****

In a GitHub repository, where must YAML workflow files be located for GitHub Actions to automatically detect and run them?

* [*] B.	.github/workflows

****

The correct option is *.github/workflows*.

GitHub Actions automatically discovers workflow YAML files when they are placed in that directory at the root of the repository. It scans for .yml or .yaml files there and runs them according to their defined triggers.

_.github/pipelines_ is not a recognized directory for workflows, so files placed there will not be picked up by GitHub Actions.

_github/workflows_ omits the required leading dot directory and is not the reserved location that GitHub Actions scans.

=== Exam Tip

When you see a path question, confirm the hidden _.github_ directory and the exact _workflows_ name in the repository root.

=== Question 30

****

In a GitHub Actions workflow with two pwsh steps where the first step runs two commands and the second runs one, how many PowerShell commands execute on the Windows runner?

* [*] C.	3

****

The correct option is *3*.

Each GitHub Actions step that uses pwsh executes the script in its run block within a PowerShell process. If the first step runs two commands and the second step runs one then the total number of commands executed on the Windows runner is the sum of those counts. Steps in a job execute in order on the same runner by default which means all of these commands run on that machine.

The option _4_ is incorrect because there are only two commands in the first step and one in the second so there is no extra command to reach that total.

The option _2_ is incorrect because both steps run and their commands are counted which makes the total greater than two.

The option _5_ is incorrect because there are no hidden or implicit commands beyond the ones you place in the run blocks of the steps.

=== Exam Tip

Count the commands inside each _run_ block and remember that _steps_ in a job execute in order on the same _runner_ unless you split work across separate jobs.

=== Question 31

****

In a private GitHub repository, which repository permission is required to delete archived GitHub Actions workflow run logs?

* [*] B.	write

****

The correct option is *write*.

GitHub requires repository *write* access to manage workflow runs and their logs. This is the least privilege that allows deletion of archived workflow run logs in private repositories.

_admin_ is not required because deleting logs does not demand full administrative control of the repository and the task can be done with the lower *write* permission.

_maintain_ is not the correct choice because the question asks for the required permission and the minimum needed is *write*. Higher roles may also be able to perform the action yet they exceed what is required.

_read_ is insufficient because view-only access does not allow managing workflow runs or deleting their logs.

=== Exam Tip

When a question asks which permission is _required_ choose the _minimum_ role that enables the action and remember that Actions management tasks typically need repository write access.

=== Question 32

****

A GitHub Actions workflow contains jobs and steps, but it never runs when commits are pushed to the main branch. Which configuration mistake would prevent it from triggering?

* [*] B.	Workflow lacks an on trigger so no event starts it

****

The correct option is *Workflow lacks an on trigger so no event starts it*.

GitHub Actions requires the on key in the workflow file to define which events start a run. If no events are listed then pushes to the main branch and any other events will never schedule the workflow even though the jobs and steps are defined.

_YAML indentation is malformed_ is not the specific cause in this scenario because a malformed workflow would fail validation and GitHub would report a syntax error rather than silently never running on push.

_The workflow file is outside .github/workflows_ would prevent GitHub from recognizing the workflow at all which means it would not appear in the Actions tab and that differs from a valid workflow that simply lacks an event trigger.

_Each run step must have a unique id_ is incorrect because step ids are optional and only needed when you want to reference a step later and they do not affect whether a workflow triggers.

=== Exam Tip

When a workflow does not run on a push, first check the _on_ key and any branch or path filters, then confirm the file is in _.github/workflows_ and that the default branch matches your trigger.

=== Question 33

****

Within a GitHub Actions workflow, what does the GITHUB_ACTIONS environment variable indicate?

* [*] B.	It is set to &quot;true&quot; only when running on GitHub Actions

****

The correct option is *It is set to "true" only when running on GitHub Actions*.

The GITHUB_ACTIONS environment variable is automatically defined by the runner when a workflow executes on GitHub Actions. When present its value is the literal string true which lets your scripts detect that they are running inside this environment. When you run the same code outside of GitHub Actions this variable is absent and the check will fail which is the intended behavior.

_It holds the REST API base URL_ is incorrect because the REST API base URL is exposed as the GITHUB_API_URL environment variable and not by GITHUB_ACTIONS.

_It contains the current run ID_ is incorrect because the current workflow run identifier is provided as GITHUB_RUN_ID and not GITHUB_ACTIONS.

=== Exam Tip

Match variable names to their purpose and look for precise wording. If an option suggests a URL or an identifier then consider _GITHUB_API_URL_ or _GITHUB_RUN_ID_ and reject answers that do not align.

=== Question 34

****

In GitHub Actions, which capability packages multiple steps into a single reusable unit without using Docker or custom JavaScript?

* [*] B.	Composite action that groups steps

****

The correct option is *Composite action that groups steps* because it packages multiple steps into one reusable unit and it does not require Docker or custom JavaScript.

A *composite action* defines its steps in an action metadata file and runs shell commands directly on the runner. A *composite action* can accept inputs and set outputs which lets you share step logic across repositories and workflows while avoiding container builds or Node setup.

_Reusable workflows_ let you call an entire workflow from another workflow and they operate at the workflow level rather than as an action. _Reusable workflows_ do not package steps into a single action unit, so they do not meet this requirement.

_Docker action_ runs inside a container and needs a Dockerfile which introduces Docker when the question requires no Docker. Therefore _Docker action_ is not suitable here.

_JavaScript action_ executes Node based code and requires custom JavaScript which the question explicitly excludes. This makes _JavaScript action_ incorrect for this scenario.

=== Exam Tip

Watch for phrases like _without Docker_ and _without custom JavaScript_. These usually point to _composite actions_. If you see _workflow_call_ or whole workflow reuse then consider reusable workflows instead.

=== Question 35

****

In a GitHub Actions workflow, what does the jobs.build_app.runs-on setting specify?

* [*] B.	It selects the runner environment and operating system for the job

****

The correct option is *It selects the runner environment and operating system for the job*. The runs-on setting in a job determines which runner type and operating system image will execute the steps in that job.

This setting chooses whether the job runs on a GitHub hosted runner such as Ubuntu, Windows, or macOS images or on a self hosted runner using labels. It applies at the job level so all steps in that job run on the selected environment.

_It defines job level environment variables_ is incorrect because job level variables are configured with the env key. The runs-on setting does not create environment variables and only selects the runner environment.

_It sets the strategy matrix for parallel builds_ is incorrect because parallelization is configured with the strategy and matrix keys. The runs-on setting does not define a build matrix and only picks the runner platform for the job.

=== Exam Tip

Match keywords to what they configure. _runs-on_ points to where the job runs, _env_ sets variables, and _strategy.matrix_ controls parallelization.

=== Question 36

****

In GitHub, where can you view the run logs to troubleshoot a failed Actions workflow on a pull request? (Choose 2)

* [*] B.	Pull request &quot;Checks&quot; tab
* [*] C.	Repository &quot;Actions&quot; tab

****

The correct options are *Pull request "Checks" tab* and *Repository "Actions" tab*.

On a pull request the *Checks tab* lists the workflow runs tied to that change and shows each job and step. You can expand the failed job to view detailed logs in context, which makes it easy to see what failed and why as part of the review.

In the repository the *Actions tab* shows all workflow runs across branches and events. You can open the failed run for the pull request and inspect the full logs or start a rerun from there.

The _Security_ area is for code scanning, secret scanning and dependency alerts, and it does not contain GitHub Actions run logs.

The _Issues_ section is for tracking work and conversations, and it does not display workflow run logs.

=== Exam Tip

If the scenario mentions a _pull request_ then think the _Checks_ tab in the PR, and if it mentions repository wide runs or history then think the _Actions_ tab. Look for keywords like jobs, steps, logs, or rerun to guide your choice.

=== Question 37

****

In a single GitHub Actions workflow, how do you define job dependencies so that qa runs after compile and release runs after qa?

* [*] B.	Set job dependencies with needs on dependent jobs

****

The correct option is *Set job dependencies with needs on dependent jobs*.

In GitHub Actions, jobs run in parallel unless you explicitly declare dependencies with needs. Define a compile job, then define a qa job that uses needs to depend on compile, and finally define a release job that needs qa. This enforces the desired execution order inside the same workflow and propagates failures so downstream jobs do not start if an upstream job fails unless you explicitly allow that behavior.

_Configure a workflow_run trigger_ is incorrect because workflow_run starts a new workflow after another workflow completes. It does not control the order of jobs within a single workflow, so it cannot make qa run after compile within the same workflow.

_Use an if condition with success() on each job_ is incorrect because an if condition does not create a dependency between jobs. Without needs, jobs can still start in parallel, and success() at the job level does not reference other jobs. You must declare dependencies with needs to guarantee ordering.

=== Exam Tip

When a question asks about ordering jobs in the same workflow, look for the keyword _needs_. If it mentions coordinating separate workflows, think _workflow_run_.

=== Question 38

****

How does the packaging and distribution of JavaScript GitHub Actions differ from that of typical Node.js applications?

* [*] C.	Dependencies are bundled and committed, and releases are tagged for GitHub Marketplace

****

The correct option is *Dependencies are bundled and committed, and releases are tagged for GitHub Marketplace*.

JavaScript actions are prepared so that their runtime code and dependencies are already present in the repository. Authors typically bundle the code into a dist directory using a bundler and commit that output. Consumers then use a tagged reference in their workflow and the author creates a release so the action can be listed and discovered in GitHub Marketplace.

This differs from typical Node.js applications where dependencies are installed at runtime from a registry. For actions the runner expects the code to be ready to execute without running npm install during the workflow.

_Published to npm and installed at runtime_ is incorrect because actions are not pulled from npm when a workflow runs. They are referenced by owner and repository with a tag and their bundled output is already committed to the repository.

_They can only call GitHub APIs and cannot reach external services_ is incorrect because actions can call any external service that the runner can reach. They frequently interact with cloud providers and third party APIs using provided credentials.

_They are packaged by Cloud Build and delivered through Artifact Registry_ is incorrect because that workflow belongs to Google Cloud services. GitHub Actions are distributed from GitHub repositories and versioned with tags and releases rather than through those services.

=== Exam Tip

When answers mention npm installation think of typical apps. For JavaScript actions look for _bundled dependencies_ and _tagged releases_ in _Marketplace_ and remember the uses pattern that references owner slash repo at a tag.

=== Question 39

****

After renaming environment variables, a GitHub Actions workflow fails. What should you check first to diagnose the issue?

* [*] B.	Review run logs and repository documentation to confirm how variables are defined and passed

****

The correct answer is *Review run logs and repository documentation to confirm how variables are defined and passed*.

This choice focuses on verifying the most likely source of failure after a rename. The run logs reveal which values were resolved at runtime and whether anything is empty or missing. Looking at repository documentation and the workflow files confirms whether a value should be a secret, a repository or environment variable, or written via GITHUB_ENV, and whether it is referenced correctly in job and step env blocks. This quickly surfaces name mismatches, wrong contexts, or scope issues without unnecessary changes.

_Enable step debug logging with ACTIONS_STEP_DEBUG and rerun_ can help after basic checks, yet it is not the first step because standard logs and a configuration review usually make variable and scoping problems obvious and avoid adding extra noise.

_Rotate the cloud provider service account key and redeploy_ addresses credential rotation and deployment processes and it does not target the common cause of failures that follow a simple variable rename. It is disruptive and should not be attempted before confirming definitions and references.

=== Exam Tip

When a question hints at renamed _variables_, choose the option that inspects _run logs_ and the configuration _first_ before enabling deeper debugging or changing credentials.

=== Question 40

****

Which GitHub Actions event triggers a workflow when a new comment is posted on an existing issue?

* [*] B.	issue_comment

****

The correct option is *issue_comment*.

The *issue_comment* event is designed to fire when a comment on an existing issue or pull request is created, edited, or deleted. If you need to run a workflow only when a new comment is added then you can filter on the created activity type so the workflow starts only for new comments.

The _discussion_comment_ event targets GitHub Discussions and triggers on comments made within discussions rather than on issues, therefore it does not match the scenario of commenting on an existing issue.

The _issues_ event tracks changes to the issue itself such as opening, closing, labeling, or editing and it does not trigger when a separate issue comment is added.

There is no _issues.comment_ event name in GitHub Actions and the correct event for issue comments is *issue_comment*.

=== Exam Tip

Match the event name to the resource being acted on and the action type. For an issue _comment_ look for the comment specific event and consider filtering on the _created_ type when you only want new comments to trigger a workflow.

=== Question 41

****

In a GitHub Actions job that uses a matrix with the keys runtime and os, how do you reference the selected values within a step?

* [*] B.	Use the matrix context like matrix.runtime and matrix.os

****

The correct option is *Use the matrix context like matrix.runtime and matrix.os*. This is how you access the selected matrix values in a job step because GitHub Actions exposes each chosen axis through the matrix context.

The matrix context carries the values chosen for the current job so you can reference runtime and os from it in expressions within run commands and also in with or env sections. If you need these values inside a shell script you can interpolate the matrix expressions or assign them to environment variables within the step.

_Use vars.runtime and vars.os_ is incorrect because the vars context holds Actions variables defined at the repository, organization, or environment level and it does not automatically track per job matrix selections unless you explicitly copy those values into variables.

_Use env.runtime and env.os_ is incorrect because the env context refers to environment variables and it is not automatically populated with matrix values. It will only contain those values if you assign them from the matrix context yourself.

=== Exam Tip

When a question mentions a build matrix look for the _matrix_ context first. Remember that _env_ and _vars_ only contain matrix values if you explicitly map them from the matrix context.

=== Question 42

****

In GitHub Actions when an environment requires reviewers, what happens to a deployment job that has been waiting for approval for 90 days?

* [*] B.	Marked as failed after 90 days without approval

****

The correct option is *Marked as failed after 90 days without approval*.

When a deployment job targets an environment with required reviewers, GitHub Actions pauses the job and waits for approval. If no reviewer approves within 90 days, the job is automatically marked as failed so the workflow has a clear terminal state and you can re-run or retrigger after addressing the reason for the delay.

_Remains waiting indefinitely_ is incorrect because GitHub enforces a maximum approval window for environment gated deployments, so jobs do not wait forever.

_Canceled after the approval window_ is incorrect because the job does not end in a cancellation state at the limit. It is marked as failed when the 90 day window expires.

=== Exam Tip

When options differ only by the final state after an approval window, focus on the defined timeout behavior. For environment approvals the job becomes _failed_ if no one approves, not indefinite and not a _cancellation_.

=== Question 43

****

What should you do to prevent a GitHub Actions workflow from running until an external API is healthy again?

* [*] C.	Disable the workflow so it does not run until the API is healthy again

****

The correct option is *Disable the workflow so it does not run until the API is healthy again*. This stops all triggers from starting new runs until you enable it again.

Disabling a workflow is the clean and reversible way to pause automation when an external dependency is down. It prevents any scheduled, event driven, or manual runs from starting, which saves minutes and avoids noisy failures. When the API is healthy again you can reenable the workflow and resume normal operation without code changes.

_Delete the workflow file from the repository_ is wrong because it is a destructive change that removes the workflow definition and history. This does not simply pause runs and it requires a commit to restore it later.

_Set continue-on-error on the API call step_ is wrong because it allows the run to proceed after a failure rather than stopping the workflow from running. The workflow would still execute and this can mask real issues.

_Edit the workflow to skip the API step until the service is back online_ is wrong because the workflow would still run and you would need another change to reenable the step later. Other steps that depend on the API could still fail.

=== Exam Tip

When a question says to stop runs entirely favor answers that _disable_ or _pause_ the workflow. If an option only lets failures pass or skips a step then the workflow still runs and that is not what the question asks.

=== Question 44

****

In a GitHub Actions workflow badge URL, which query parameter displays the status of a specific branch?

* [*] B.	?branch=release-25-03

****

The correct option is *?branch=release-25-03* because the workflow status badge uses the branch query parameter to display the status for a specific branch.

When you add *?branch=release-25-03* to the badge URL, GitHub renders the badge for that exact branch instead of the default branch. This is the documented way to select which branch the badge reflects.

_?event=push_ is incorrect because it filters the badge by the workflow trigger event type rather than by branch, so it does not target a specific branch.

_?ref=main_ is incorrect because ref is not a supported query parameter for workflow badge URLs and is used in other contexts, so it will not display a branch specific badge.

=== Exam Tip

When a question asks how to target a branch in a GitHub Actions badge, look for the parameter that literally says _branch_ and avoid confusing it with _event_ or _ref_.

=== Question 45

****

A JavaScript GitHub Action intermittently fails within the first 60 seconds on a hosted runner. What is the quickest initial step to determine what failed and why?

* [*] C.	Open the workflow run and read the failed step logs for errors

****

The correct answer is *Open the workflow run and read the failed step logs for errors*. This is the fastest way to see exactly which command failed, what error was printed, and the exit code that GitHub recorded without changing the workflow or rerunning the job.

Opening the run and inspecting the failed step gives immediate context such as timestamps, the specific action output, and any stack traces. This is especially helpful for intermittent failures in the first minute on a hosted runner because the default logs already include the information you need to pinpoint the failing step and start remediation.

_Enable step debug logs with ACTIONS_STEP_DEBUG_ is not the quickest first step because it requires enabling a setting or adding a secret and then rerunning the workflow to capture the extra verbosity. It is useful when the standard logs do not provide enough detail, but you should first read what the failed step already reported.

_Switch the JavaScript action to a Docker container action_ is not a diagnostic step and it adds complexity and runtime overhead on a hosted runner. Changing the action type does not explain why the failure occurred and it can introduce new variables that make troubleshooting slower.

=== Exam Tip

Start with the _default logs_ of the failed step to get quick evidence, then escalate to _debug logging_ only if the baseline output is insufficient.

=== Question 46

****

When selecting the operating system for a GitHub Actions runner to execute workflows, which factor should primarily guide the choice?

* [*] B.	OS compatibility with required tooling and dependencies

****

The correct option is *OS compatibility with required tooling and dependencies*.

You should choose the runner operating system that matches the software stack your workflow needs. Actions and scripts must run where the language runtimes, package managers, native libraries and system services they require are available and supported. This ensures reliable builds and tests with fewer environment related failures. For example if your workflow needs Xcode you use macOS. If it requires a Windows only build tool you use Windows. If it installs packages with apt or runs Linux containers then Ubuntu is a natural fit.

_Team OS familiarity_ is not a primary driver because workflows run in isolated runners that do not depend on the developer workstation. Familiarity may help productivity or troubleshooting but it does not determine whether the job can execute successfully.

_Workflow minutes cost_ should not be the primary factor because the job must first run on an operating system that supports its tools and dependencies. Cost can be a secondary consideration only when multiple operating systems meet the requirements.

=== Exam Tip

Anchor your choice to the workflow _requirements_ by listing tools and _dependencies_ first, then pick the runner OS that provides native _compatibility_. Treat cost or preferences as _tie breakers_ only.

=== Question 47

****

In a GitHub Actions job log, what information is shown in the "Set up job" section? (Choose 3)

* [*] B.	GITHUB_TOKEN permissions
* [*] C.	Runner image
* [*] E.	Operating system

****

The correct options are *GITHUB_TOKEN permissions*, *Runner image*, and *Operating system*.

In the Set up job step, *GITHUB_TOKEN permissions* are shown so you can verify the scopes that the workflow will use. This helps confirm that the token has the expected level of access for the job.

The same section lists the *Runner image* which identifies the virtual environment used by the runner and it also shows the *Operating system* that the job is running on. This makes it easy to confirm the runtime platform before any steps execute.

_Repository secrets list_ is not displayed in this section. GitHub never prints secret values in logs and the setup output does not enumerate repository secrets.

_Code scanning results_ do not appear in the setup phase. Those results are produced by later steps that run analysis tools and they are surfaced in separate logs and alerts.

=== Exam Tip

When a question references the Set up job output, think about environment details and _permissions_ rather than results or _secrets_. Expect information about the runner and token configuration, not analysis findings.

=== Question 48

****

How should a maintainer describe and categorize a GitHub Action in the GitHub Marketplace to maximize discoverability and clarity?

* [*] C.	Use a clear and concise description and choose one most relevant category

****

The correct option is *Use a clear and concise description and choose one most relevant category*.

A short and clear description helps people quickly grasp what the action does and it improves how it appears in search and browse results in the Marketplace. Choosing the one category that best fits matches how Marketplace filters work which places the listing where interested users expect to find it and keeps the focus on its primary purpose.

Comprehensive details belong in the README so the Marketplace listing should highlight the value in a brief summary that encourages clicks without overwhelming readers.

_Add many unrelated topics and keywords to broaden reach_ is incorrect because irrelevant topics and keyword stuffing reduce result quality and can violate Marketplace policies which expect accurate and non misleading listings.

_Provide a long feature list to attract many teams_ is inaccurate because lengthy descriptions make scanning harder and do not improve ranking and users rely on concise summaries in the Marketplace and on detailed documentation in the repository for the rest.

=== Exam Tip

When options compete between breadth and focus choose the one that favors _concise_ wording and a _single_ most _relevant_ category while leaving details to documentation.

=== Question 49

****

What is the minimum supported cron schedule interval for GitHub Actions workflows?

* [*] B.	Five minute interval

****

The correct option is *Five minute interval*.

GitHub Actions supports scheduled workflows with cron expressions and enforces a minimum time between runs of five minutes. Even if a cron expression specifies a shorter cadence the workflow will not run more frequently than that minimum.

_Every fifteen minutes_ is not the shortest interval because the platform allows schedules to run more frequently than fifteen minutes. Therefore it cannot be the correct choice for the shortest supported interval.

_Every one minute_ is not supported because GitHub Actions does not allow schedules to run more often than every five minutes. Any attempt to schedule at one minute intervals will not execute at that frequency.

=== Exam Tip

When a question asks for the shortest or maximum interval focus on documented _limits_ rather than what cron can express. Verify the platform _enforcement_ rules in the vendor docs.

=== Question 50

****

In a single GitHub Actions step, what happens when the "continue-on-error" key is set and the step fails?

* [*] B.	It lets the workflow proceed even when that step fails

****

The correct option is *It lets the workflow proceed even when that step fails*.

When you set continue-on-error on a step, a non zero exit from that step marks only the step as failed while the job keeps running the subsequent steps. The job is not failed solely because of that step, so downstream jobs that need this job can still run and the workflow can continue.

_It forces the step to run every time regardless of earlier failures or conditions_ is wrong because that describes unconditional execution using an if expression with the always function. Continue-on-error does not control whether a step runs. It only changes what happens after the step fails.

_It sets the job-level continue-on-error so the whole job can fail without failing the workflow_ is wrong because the step setting does not change job behavior. Job level continuation is configured on the job itself and is separate from a step level setting.

_It disables fail fast behavior for matrix jobs so parallel runs are not cancelled_ is wrong because matrix cancellation is managed by the matrix strategy fail fast setting, not by a step level key.

=== Exam Tip

Look for the _scope_ in the question. If a key is set on a _step_ then it only affects that step. Compare step, job, and matrix settings to eliminate options that apply at the wrong level.

=== Question 51

****

Before submitting a GitHub Action to the GitHub Marketplace, which repository requirement must be met?

* [*] C.	Keep the action metadata file at the repository root

****

The correct option is *Keep the action metadata file at the repository root*.

GitHub identifies an action by reading the action.yml or action.yaml file and requires it to be discoverable at the top level of the repository. Marketplace validation expects this structure, so an action is only recognized for listing when *the action metadata file is at the repository root*.

_Enable GitHub Pages for the repository_ is unrelated to publishing an action in GitHub Marketplace and has no effect on action discovery or eligibility.

_Host the action in a private repository_ is not acceptable for Marketplace listings because actions must be in public repositories for users to find and use them.

_Place the action metadata file inside an actions subdirectory_ is incorrect because GitHub looks for the metadata file in the repository root rather than in a nested directory.

=== Exam Tip

When options compare file locations, watch for keywords like _root_ versus _subdirectory_ and confirm them against vendor requirements. Also verify whether the repository must be _public_ when Marketplace is involved.

=== Question 52

****

How can you limit repository access to specific self-hosted runner pools while maintaining isolation between departments?

* [*] B.	Create runner groups with repository access controls

****

The correct option is *Create runner groups with repository access controls*.

*Runner groups* let you place self hosted runners into a defined group at the organization or enterprise level and then you grant explicit repository access to that group. Only the repositories you allow can target those runners, which enforces departmental isolation and prevents unintended repositories from using the same compute. These access controls are the built in mechanism for scoping runner pools to chosen repositories, which is exactly what the question asks for.

_Add labels to self-hosted runners and reference those labels in runs-on_ is not correct because _labels_ only help a job select among runners that the repository can already use. They do not restrict which repositories can access a runner pool, so they cannot enforce isolation across departments.

_Required workflows_ are policy workflows that ensure certain checks or configurations are present across repositories. They do not control which repositories can target specific self hosted runners, so _Required workflows_ will not isolate runner pools.

_GitHub Environments with required reviewers_ protect deployments by requiring approvals and by controlling secrets. They do not gate which repositories can run jobs on a particular set of self hosted runners, so _GitHub Environments with required reviewers_ does not solve repository scoped runner access.

=== Exam Tip

When a question asks about restricting which repositories can use a runner pool, look for controls that change _repository access_ to runners such as _runner groups_. If an option only influences job selection like _labels_ or gates deployments like environments, it will not provide repository level isolation.

=== Question 53

****

When a GitHub Actions job specifies multiple custom labels in the runs on field, how must a self-hosted runner's labels match for the job to be assigned to it?

* [*] D.	Runner must include every listed label

****

The correct option is *Runner must include every listed label*.

When a job specifies multiple labels in runs-on for self-hosted runners, GitHub Actions applies logical AND matching. A runner is eligible only if it has all the labels that you list in the workflow. This ensures you can target runners that meet every required characteristic and prevents selection of runners that are missing any requirement.

_Runner groups decide routing not labels_ is incorrect because runner groups control which repositories or organizations can use a set of runners while the actual selection of a runner for a job relies on label matching from runs-on.

_Labels are auto assigned from OS and hardware_ is incorrect in this context because the question asks about how matching works. While self-hosted runners include some default labels and you can add custom ones, the matching rule still requires that all labels listed in runs-on must be present on the runner.

_Any one matching label is enough_ is incorrect because matching is not logical OR. A runner that matches only one of several labels will not be selected for the job.

=== Exam Tip

When runs-on lists multiple labels, read it as an _AND_ checklist where _all_ labels must be present on the self-hosted runner. The order of labels does not matter.

=== Question 54

****

In GitHub Actions workflows, how should you reference third party actions to keep pipelines stable while adopting updates safely?

* [*] C.	Pin to a major version then refine to a minor tag or commit when needed

****

The correct option is *Pin to a major version then refine to a minor tag or commit when needed*.

This approach begins with a stable major tag such as v3 so you automatically receive compatible minor and patch updates that include fixes and security improvements. You then lock down further only when needed by moving to a specific minor tag or a verified commit SHA after testing. This keeps pipelines predictable while still adopting improvements in a controlled way.

_Use the latest tag_ is risky because the tag is mutable and can change without notice which can introduce breaking changes or unreviewed code. It reduces reproducibility and can destabilize workflows.

_Use the action's default branch_ follows ongoing development and can include breaking changes or experimental commits. It is not a versioned reference and it can change at any time which harms stability.

_Use the newest commit SHA_ does not provide a stable reference because it chases the most recent change. While pinning to a specific commit SHA is a secure practice, automatically jumping to the newest commit removes the controlled update process that keeps pipelines stable.

=== Exam Tip

Look for options that balance _stability_ with controlled updates. Prefer approaches that use a versioned reference and allow you to _tighten_ to a specific commit after testing, and be wary of words like _latest_ or _default branch_ which usually mean mutability.

=== Question 55

****

When a push trigger specifies both branch and path filters, under what condition does the workflow run?

* [*] C.	It runs only when both branch and path filters match

****

The correct answer is *It runs only when both branch and path filters match*.

For a push event in GitHub Actions, when you specify both branch filters and path filters, the event must satisfy both sets of conditions. The pushed ref must match one of the branch patterns and at least one of the changed files in the push must match the path patterns. If either side does not match, the workflow does not run.

_Filters are evaluated in order and the first match triggers_ is incorrect because the filters are not processed with a first match wins approach. They are evaluated independently and must meet the documented matching rules rather than stopping at the first match.

_It runs when either the branch pattern or the path pattern matches_ is incorrect because that describes an either or condition. The push trigger uses a both must match rule when branches and paths are configured together.

_Path filters apply only to pull requests so push uses only branches_ is incorrect because the push event supports paths and paths-ignore, and these filters are commonly used to restrict workflows to certain files on push.

=== Exam Tip

When multiple filters are defined for the same event, remember that matching is typically an _AND_ across different filter types and an _OR_ within the values of the same filter. Read the event section to confirm how branches and paths interact.

=== Question 56

****

Which statements accurately describe the practical differences between GitHub hosted runners and self hosted runners in GitHub Actions? (Choose 3)

* [*] A.	Self hosted runners often persist and retain tools and caches between jobs
* [*] C.	GitHub hosted runners use a fresh virtual machine for every job so runs start clean
* [*] D.	Self hosted runners can reach internal networks while GitHub hosted runners cannot by default

****

The correct options are *Self hosted runners often persist and retain tools and caches between jobs*, *GitHub hosted runners use a fresh virtual machine for every job so runs start clean*, and *Self hosted runners can reach internal networks while GitHub hosted runners cannot by default*.

*Self hosted runners often persist and retain tools and caches between jobs* because the machine is long lived under your control. You can install software and keep files or caches on disk across multiple runs which can speed builds and enable custom tooling. This persistence also means you must handle cleanup and isolation to avoid unintended state leaks.

*GitHub hosted runners use a fresh virtual machine for every job so runs start clean* since each job is provisioned on a new ephemeral environment. This provides strong isolation and reproducibility because no filesystem state or processes carry over from prior jobs. Tools come from the preinstalled image or are set up during the job which keeps the environment predictable.

*Self hosted runners can reach internal networks while GitHub hosted runners cannot by default* because self hosted machines run inside your infrastructure where they can access private subnets and services directly. GitHub hosted machines run in GitHub managed infrastructure and by default do not have direct connectivity to your private network unless you add an approved private networking approach or similar integration.

_GitHub hosted runners have default access to private VPC resources_ is incorrect because they do not automatically connect to your internal networks. You must either use a self hosted runner in that network or configure an allowed private networking solution to reach those resources.

=== Exam Tip

Identify what runs where and think about _isolation_ and _network reachability_. If a statement implies persistence or private access then it usually points to self hosted. If a statement emphasizes clean environments then it usually points to GitHub hosted.

=== Question 57

****

In GitHub Actions caching, what is the purpose of the restore-keys setting when the primary cache key is not found?

* [*] B.	Provide fallback key prefixes tried in order

****

The correct option is *Provide fallback key prefixes tried in order*.

When the primary cache key does not match, this setting supplies a list of prefixes that the cache action checks one by one. For each prefix it looks for an existing cache whose key begins with that prefix and restores the most recently created match. This provides a graceful fallback to a close match so jobs can reuse a partially relevant cache instead of starting from scratch.

_Allow cross-OS cache reuse_ is incorrect because caches are scoped to the runner environment which includes the operating system. This setting does not enable sharing caches across different operating systems.

_Set fail-on-cache-miss behavior_ is incorrect because whether a miss should fail the step is controlled by a separate input on the cache action. The restore key setting does not change failure behavior.

=== Exam Tip

When you see _restore-keys_ think ordered prefix matching. Read the keys from most specific to least specific and confirm that they would still provide a useful cache if the _primary key_ misses.

=== Question 58

****

In a GitHub Actions workflow that runs a Docker container action, the entrypoint.sh script fails with a permission denied error. What is the simplest change to ensure the script runs?

* [*] B.	Run chmod +x on entrypoint.sh before the container action runs

****

The correct option is *Run chmod +x on entrypoint.sh before the container action runs*.

The error occurs because the script file is missing the executable bit. Making sure the file is executable before the container starts allows the operating system to run it without a permission denied error and it is the smallest and most direct change you can make in the workflow. Adding a step that sets the executable bit ensures the container action can invoke the script successfully.

The option _Use a composite action instead of a Docker action_ is incorrect because changing the action type does not address the missing executable bit and it introduces unnecessary complexity without solving the underlying permissions issue.

The option _Switch to a different entry point script_ is incorrect because the problem is the permission on the current script and picking another file does not guarantee it will be executable and it changes behavior without fixing the root cause.

=== Exam Tip

When a workflow script fails with _permission denied_, check the _executable bit_ first and consider a quick step that runs _chmod +x_ or commit the permission change so it persists.

=== Question 59

****

When repository settings are left at their defaults, how long are GitHub Actions workflow run logs and artifacts retained?

* [*] B.	90 days

****

The correct option is *90 days*. This is the default retention period GitHub applies to workflow run logs and to artifacts when the repository settings are not changed.

Artifacts are stored for *90 days* by default and are then expired unless you configure a different retention period in the repository or organization settings or set a value in a workflow. Workflow run logs follow the same default of *90 days* unless you override it.

_1 year_ is not the default. You can raise the retention period in settings depending on your plan, yet it does not start at _1 year_.

_Indefinitely_ is not correct because GitHub does not keep logs or artifacts forever by default. Expiration is enforced unless you change the retention policy.

_30 days_ is shorter than the default. Unless you lower the setting, GitHub keeps workflow run logs and artifacts for *90 days*.

=== Exam Tip

Look for the words _default_ and _repository settings_. If nothing is changed, remember GitHub Actions keeps workflow logs and artifacts for _90 days_.

=== Question 60

****

In a GitHub Actions job running on an Ubuntu runner, how can you add /opt/cli to the PATH so it is available in all subsequent steps?

* [*] B.	Echo &quot;/opt/cli&quot; to $GITHUB_PATH in a run step

****

The correct option is *Echo "/opt/cli" to $GITHUB_PATH in a run step*.

Writing the directory to *$GITHUB_PATH* uses the Actions environment files feature and the runner automatically appends that directory to PATH for the remainder of the job. This persists across all later steps in the job on the Ubuntu runner without any additional export commands.

_Set PATH in a job-level env_ is not the supported way to add a directory for following steps. The runner reinitializes PATH for each step and the documented method to persist additions across steps is the special environment file for PATH.

_Append "/opt/cli" to $GITHUB_STEP_SUMMARY in a run step_ is unrelated to environment setup because that file produces the job or step summary shown in the interface and it does not change PATH.

_Append "/opt/cli" to $GITHUB_ENV in a run step_ is incorrect because that file expects lines in a key equals value format to define environment variables. Appending a bare directory string would not modify PATH and would instead create an invalid entry. The supported method for extending PATH across steps is the dedicated PATH environment file.

=== Exam Tip

When a question asks to persist a change to _PATH_ for later steps, look for the special environment file and choose _$GITHUB_PATH_. Use _$GITHUB_ENV_ for key value variables and remember that _$GITHUB_STEP_SUMMARY_ only affects the summary shown in the interface.

=== Question 61

****

How can a team prevent containerized self-hosted ephemeral runners from updating while jobs are running and maintain control over when the runner image is upgraded?

* [*] B.	Disable runner self update and pin the runner version in the container image

****

The correct option is *Disable runner self update and pin the runner version in the container image*.

This approach keeps the runner binary immutable during job execution which avoids unexpected restarts or behavior changes while a workflow is running. You control upgrades by rebuilding the container image with a known runner release and then rolling out that new image on your schedule. This is a common best practice for ephemeral containerized runners because each job starts from a clean image that already contains the vetted runner version.

_GitHub-hosted runners_ are fully managed by GitHub and do not let you control the runner image or update cadence, and the question targets self-hosted ephemeral containers where you manage the image yourself.

_Enable automatic runner updates_ would allow the runner to update itself during execution which removes your control over when the update happens and can interrupt or change the environment mid job.

=== Exam Tip

When a question stresses keeping control over upgrades for self hosted or _ephemeral_ containers look for answers that say to _disable self update_ and to _pin_ a specific runner version in the image.

=== Question 62

****

In the GitHub Actions run interface, how can you share a direct link to a specific line in the step log?

* [*] B.	Create a permalink from the line number in the step log

****

The correct option is *Create a permalink from the line number in the step log*.

Within the run interface you can open the job and step, hover over the line number, and use the user interface to copy a URL that anchors directly to that exact log line. Sharing that URL opens the run log to the chosen step and highlights the selected line so the recipient lands on the precise context.

_Download the logs and email the file_ is incorrect because it does not provide a direct link inside the run interface and it requires the recipient to handle an external file without any anchored line reference.

_Grant write access so the run logs can be opened_ is incorrect because granting write permissions does not create a shareable deep link to a specific line and logs are typically viewable with appropriate read access in the repository.

_Share a GitHub Gist of the line_ is incorrect because a Gist is separate from the run interface and does not open the Actions log view at the exact line within the workflow run.

=== Exam Tip

When a question asks for a direct link inside the GitHub Actions run view look for the built in _permalink_ option near the log _line number_ rather than any workaround outside the interface.

=== Question 63

****

In GitHub Actions workflows, which YAML rules govern indentation and line breaks?

* [*] C.	YAML is whitespace sensitive and forbids tab indentation and it is a superset of JSON

****

The correct option is *YAML is whitespace sensitive and forbids tab indentation and it is a superset of JSON*.

GitHub Actions workflows are written in YAML which means indentation and line breaks define structure. YAML requires spaces for indentation and tabs are not allowed for indentation. Line breaks and consistent spacing determine how mappings and sequences are nested. YAML is also a superset of JSON which means valid JSON is valid YAML even though workflow files are authored as YAML and must follow YAML spacing rules.

_Tabs and spaces can be mixed if indentation levels stay consistent_ is incorrect because YAML does not allow tabs for indentation and expects spaces which means mixing tabs and spaces for structural indentation is not permitted.

_GitHub Actions workflows use JSON so line breaks are insignificant_ is incorrect because workflows use YAML rather than JSON and YAML is whitespace sensitive so both indentation and line breaks carry meaning.

=== Exam Tip

When a question mentions GitHub Actions workflow files, think in _YAML_ and confirm _no tabs_ and that indentation and line breaks define structure.

=== Question 64

****

In GitHub Actions, what is the primary purpose of committing pinned dependencies only on release tags and triggering builds only during the release event?

* [*] B.	Improve supply chain security by pinning at tag and building on release

****

The correct option is *Improve supply chain security by pinning at tag and building on release*.

This approach reduces the risk of unexpected dependency changes because the exact versions are captured at the moment you create a release. It also helps ensure reproducible builds since the workflow runs when a release is cut and uses the pinned dependencies to produce artifacts that match what consumers will download. Limiting privileged build steps to the release event narrows exposure to secrets and provenance issues and aligns the final artifact with verifiable and consistent inputs.

_Run builds on all branches_ is incorrect because building everywhere prioritizes coverage and speed rather than the security goal of producing artifacts only from a controlled release process with pinned inputs.

_Discourage use of tags or SHAs by consumers_ is incorrect because security guidance encourages the opposite. Consumers should pin to trusted tags or commit SHAs to avoid supply chain drift and tampering.

_Commit lockfiles to the main branch for faster feedback_ is incorrect because the practice in question is to commit pinned dependencies on release tags so that the versions used for the published artifact are captured at release time rather than optimized for day to day feedback speed.

=== Exam Tip

When a question mentions _pinning_ and building only on _release_ events, think _supply chain security_ and _reproducibility_ rather than speed or branch coverage.

=== Question 65

****

When should you use a hybrid of GitHub hosted runners and self hosted runners to optimize cost and developer feedback time?

* [*] B.	Use a hybrid when workloads mix quick checks with compute heavy builds and you want balanced cost and speed

****

The correct option is *Use a hybrid when workloads mix quick checks with compute heavy builds and you want balanced cost and speed*.

This approach pairs GitHub hosted runners for short linting and unit tests so developers get rapid feedback with self hosted capacity for resource intensive builds and long integration tests so you control cost for heavy work. By letting the fast jobs run on hosted machines as needed while reserving dedicated hardware for the expensive stages you reduce queue times and avoid overpaying for large instances when they are not needed.

_Use only GitHub Actions larger runners for all jobs_ is not optimal because small checks do not need high memory or many cores and forcing every task onto the largest machines increases cost without improving feedback time for quick jobs.

_Use a hybrid when every job must be isolated and security overrides performance and cost_ is not the right strategy because when strict isolation is the top priority teams often prefer fully self hosted runners with hardened controls or only ephemeral hosted runners and they accept the extra expense and slower feedback rather than mixing environments to optimize cost.

=== Exam Tip

Look for cues about mixed workloads and balance between _cost_ and _feedback time_. If the scenario blends quick checks with heavy builds then a hybrid of hosted and self hosted runners is the likely answer.
