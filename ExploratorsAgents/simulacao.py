def simular(env, agentes, grid):
    """Simula o comportamento dos agentes."""
    while True:
        for agente in agentes:
            agente.agir(grid)
        yield env.timeout(1)
