from agents import AgentManager


def main():
    manager = AgentManager()
    results = manager.run_all()

    print('Agent initialization and baseline run')
    for result in results:
        print(f"{result['agent']}: steps={result['steps']}, final_money={result['final_money']}, total_reward={result['total_reward']:.2f}")
        print(f"  metrics={result['metrics']}")


if __name__ == '__main__':
    main()
