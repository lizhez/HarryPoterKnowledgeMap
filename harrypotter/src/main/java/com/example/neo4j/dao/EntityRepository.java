package com.example.neo4j.dao;

import com.example.neo4j.entity.Entity;
import org.springframework.data.neo4j.annotation.Query;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EntityRepository extends Neo4jRepository<Entity,Long> {
    @Query(value = "MATCH (n:entity{name:$name}) RETURN n")
    public Entity getNameByName(String name);
}
