variable "project_id" {
  description = "The Google Cloud project ID"
  type        = string
  default     = "project-452e74c0-919a-47bd-903"
}

variable "region" {
  description = "GCP region for resources"
  type        = string
  default     = "europe-north1" # Stockholm region
}

variable "service_name" {
  description = "Name of the Cloud Run service"
  type        = string
  default     = "devops-app"
}

variable "image" {
  description = "Container image to deploy initially"
  type        = string
  default     = "europe-north1-docker.pkg.dev/project-452e74c0-919a-47bd-903/devops-repo/app:v1"
}