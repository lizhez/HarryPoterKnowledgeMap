package com.example.neo4j.entity;

import lombok.Data;
import org.neo4j.ogm.annotation.GeneratedValue;
import org.neo4j.ogm.annotation.Id;
import org.neo4j.ogm.annotation.NodeEntity;
import org.neo4j.ogm.annotation.Property;


import java.io.Serializable;

@Data
@NodeEntity(label = "entity")
public class Entity{
    @Id
    @GeneratedValue
    private Long id;
    @Property
    private String name;
    @Property
    private String meta;
    @Property
    private String nickname;
    @Property
    private String player;
    @Property
    private String appearance;
    @Property
    private String birthday;
    @Property
    private String magicstick;
    @Property
    private String sex;
    @Property
    private String character;
    @Property
    private String url;
    @Property
    private String video;
    @Property
    private String images;
    private String symbol="symbol";
    private int category=0;

}
