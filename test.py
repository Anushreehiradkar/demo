import psutil

# Get all processes and sort by memory usage
processes = sorted(psutil.process_iter(['pid', 'name', 'memory_percent']), key=lambda p: p.info['memory_percent'], reverse=True)

# Print top 5 memory-consuming processes
print(f"{'PID':<10} {'Memory%':<10} {'Process Name'}")
print("=" * 40)
for proc in processes[:5]:
    print(f"{proc.info['pid']:<10} {proc.info['memory_percent']:.2f}%     {proc.info['name']}")
