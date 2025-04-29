import random
import json

# === Template data ===

titles = [
    "App Service Restarting Unexpectedly",
    "App Service Slow Response Times",
    "Deployment Failures on Azure App Service",
    "App Service SSL/TLS Certificate Errors",
    "High Memory Usage in App Service",
]

descriptions = [
    "Customer reports that the app hosted on Azure restarts randomly several times per day.",
    "Customer notes significant delays loading web pages during peak traffic hours.",
    "Customer says their deployment pipeline fails when pushing to Azure App Service.",
    "Customer receiving SSL errors accessing secure endpoints.",
    "Customer reports memory usage hitting limits causing crashes.",
]

root_causes = [
    "Memory pressure causing app pool recycling.",
    "Auto-scaling rules misconfigured leading to slow response under load.",
    "Deployment credentials expired or missing deployment slot configuration.",
    "SSL Certificate expired or not properly bound to App Service.",
    "Memory leaks due to unoptimized code in hosted application."
]

azure_commands = [
    "az webapp show --name <app-name> --resource-group <rg-name>",
    "az webapp log tail --name <app-name> --resource-group <rg-name>",
    "az webapp restart --name <app-name> --resource-group <rg-name>",
    "az webapp config ssl bind --certificate-thumbprint <thumbprint> --ssl-type SNI",
]

docs = [
    {"title": "Monitor and troubleshoot Azure App Service", "link": "https://learn.microsoft.com/en-us/azure/app-service/overview-monitoring"},
    {"title": "Configure SSL bindings in Azure App Service", "link": "https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate"},
    {"title": "Scale App Service apps manually or automatically", "link": "https://learn.microsoft.com/en-us/azure/app-service/manage-scale"},
    {"title": "Deploy best practices for Azure App Service", "link": "https://learn.microsoft.com/en-us/azure/app-service/deploy-best-practices"},
]

eli5_explanations = [
    "Your app is like a car that gets overheated and needs to stop to cool down (memory limits).",
    "Your app is like a small shop getting too many customers at once (scale issues).",
    "Your app lost its key to deploy packages properly (deployment configuration issue).",
    "Your app's badge to enter the building expired (SSL certificate expired).",
]

# === Synthetic Inquiry Generator ===

def generate_inquiry():
    description = random.choice(descriptions)
    inquiry = {
        "messages": [
            {"role": "system", "content": "You are an expert Azure App Service Support Assistant."},
            {"role": "user", "content": description},
            {"role": "assistant", "content": {
                "rootCauses": [
                    {
                        "hypothesis": random.choice(root_causes),
                        "confidence": round(random.uniform(0.7, 0.95), 2),
                        "actions": [
                            "Review Azure Monitor Metrics.",
                            "Check App Service Plan scaling settings."
                        ],
                        "docs": [random.choice(docs)]
                    }
                ],
                "azureCommands": random.sample(azure_commands, 2),
                "eli5Explanation": random.choice(eli5_explanations)
            }}
        ]
    }
    return inquiry

def generate_dataset(filename, count=300):
    with open(filename, 'w') as f:
        for _ in range(count):
            inquiry = generate_inquiry()
            json.dump(inquiry, f)
            f.write('\n')

if __name__ == "__main__":
    generate_dataset("synthetic_inquiries.jsonl", count=300)
    print("✅ 300 synthetic inquiries generated successfully: synthetic_inquiries.jsonl")
