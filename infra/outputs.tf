output "vpc_id" {
  value = module.vpc.vpc_id
}

output "public_subnet_ids" {
  value = module.vpc.public_subnet_ids
}

output "private_subnet_ids" {
  value = module.vpc.private_subnet_ids
}
output "alb_sg_id" { value = module.security_groups.alb_sg_id }
output "ecs_sg_id" { value = module.security_groups.ecs_sg_id }
output "rds_sg_id" { value = module.security_groups.rds_sg_id }
output "ecs_execution_role_arn" { value = module.iam.ecs_execution_role_arn }
output "ecs_task_role_arn"      { value = module.iam.ecs_task_role_arn }
output "alb_dns_name"    { value = module.alb.alb_dns_name }
output "db_endpoint"     { value = module.rds.db_endpoint }
output "ecs_cluster"     { value = module.ecs.cluster_name }
output "ecs_service"     { value = module.ecs.service_name }
output "log_group"       { value = module.ecs.log_group_name }