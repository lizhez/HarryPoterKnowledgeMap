package com.example.neo4j.dao;

import com.example.neo4j.entity.Relation;
import org.springframework.data.neo4j.annotation.Query;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RelationRepository extends Neo4jRepository<Relation,Long> {

    @Query(value = "MATCH p=(n:entity{name:$name1})-[r:`关系`]->(s:entity{name:$name2}) RETURN p")
    public List<Relation> getRelationBetweenTwo(String name1, String name2);

    @Query(value = "MATCH p=(n:entity{name:$name})-[r:`关系`]->() RETURN p")
    public List<Relation> getRelationOfOne(String name);

    @Query(value = "MATCH p=(n:entity{name:$name})-[r:`关系`{label:$relation}]->() RETURN p")
    public List<Relation> getRelations(String name, String relation);
}
