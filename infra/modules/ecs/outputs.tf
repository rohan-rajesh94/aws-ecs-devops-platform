output "cluster_name"       { value = aws_ecs_cluster.main.name }
output "service_name"       { value = aws_ecs_service.app.name }
output "log_group_name"     { value = aws_cloudwatch_log_group.app.name }
output "prometheus_service" { value = aws_ecs_service.prometheus.name }
output "grafana_service"    { value = aws_ecs_service.grafana.name }