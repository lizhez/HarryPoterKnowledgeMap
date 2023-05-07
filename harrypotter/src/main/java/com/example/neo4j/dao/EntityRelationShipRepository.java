package com.example.neo4j.dao;

import com.example.neo4j.entity.EntityRelationShip;
import org.springframework.data.neo4j.annotation.Query;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface EntityRelationShipRepository extends Neo4jRepository<EntityRelationShip,Long> {
    @Query(value = "MATCH (n:entityRelation{target:$club}) RETURN n")
    public List<EntityRelationShip> getRelationOfClub(String club);

    @Query(value = "MATCH (n:entityRelation) WHERE n.source=$source AND n.target=$target AND n.label=$label RETURN n")
    public EntityRelationShip getRelation(String source,String target,String label);
}
