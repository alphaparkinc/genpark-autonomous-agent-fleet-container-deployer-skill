from client import AutonomousAgentFleetContainerDeployerClient

def main():
    client = AutonomousAgentFleetContainerDeployerClient()
    cfg = {"agent_image": "genpark-agent-runtime:v2.0", "replicas": 12}
    res = client.deploy_agent_fleet(cfg, "us-west-2")
    print(f"Status: {res['fleet_status']}")
    print(f"Containers Deployed: {res['deployed_containers_count']}")
    print(f"Health Check: {res['health_check_url']}")

if __name__ == "__main__":
    main()
