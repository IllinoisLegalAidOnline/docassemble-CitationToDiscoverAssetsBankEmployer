def name_or_agent(entity):
  if entity.know_agent:
    return entity.agent.name_full()
  else:
    return entity.name_full()