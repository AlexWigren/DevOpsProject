terraform {

    required_version = ">= 1.5.0"
  required_providers {
    google={
        source = "hashicorp/google"
        version = "~> 5.0"
    }
  }
}

provider "google" {
    project = var.project_id
    region = var.region
}

resource "google_artifact_registry_repository" "repo" {
    location      = var.region
    repository_id = "devops-repo"
    description   = "Docker repository for DevOps application"
    format        = "DOCKER"
}

resource "google_cloud_run_v2_service_iam_member" "public_access" {
  
  project  = var.project_id
  location = google_cloud_run_v2_service.app.location
  name     = google_cloud_run_v2_service.app.name
  role     = "roles/run.invoker"
  member   = "allUsers"    

}


resource "google_cloud_run_v2_service" "app" {
  name                = var.service_name
  location            = var.region
  ingress             = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = var.image

      ports {
        container_port = 8000
      }


      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
      }
    }
  }
}