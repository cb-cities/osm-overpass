"use strict";
//EBMUD pipeline

const tileSize = 0.01;
const baseClientTileSize = 900;

// the coordinate range limit
const firstTileX = -122.50000000000000;
const firstTileY = 37.50000000000000;
const lastTileX = -121.80000000000000; 
const lastTileY = 38.200000000000000;

const tileCountX = (lastTileX - firstTileX) / tileSize + 1;
const tileCountY = (lastTileY - firstTileY) / tileSize + 1;

const maxRoadNodeCount = 300000;
const maxRoadLinkCount = 200000;
const maxRoadLinkPointCount = 1500000;
const maxRoadLinkIndexCount = 200000;
const maxRoadCount = 200000;
const maxAddressCount = 200000;

const quadtreeLeft = -122.50000000000000;
const quadtreeTop = 37.50000000000000;
const quadtreeSize = 13.1072;


module.exports = {
  tileSize: tileSize,
  baseClientTileSize: baseClientTileSize,

  firstTileX: firstTileX,
  firstTileY: firstTileY,
  lastTileX: lastTileX,
  lastTileY: lastTileY,

  tileCountX: tileCountX,
  tileCountY: tileCountY,

  totalWidth: tileCountX * tileSize,
  totalHeight: tileCountY * tileSize,
  totalBaseClientWidth: tileCountX * baseClientTileSize,
  totalBaseClientHeight: tileCountY * baseClientTileSize,

  maxGeometryItemCount: maxRoadNodeCount + maxRoadLinkCount + maxRoadCount + maxAddressCount,
  maxVertexCount: maxRoadNodeCount + maxRoadLinkPointCount,
  maxRoadNodeCount: maxRoadNodeCount,
  maxRoadLinkCount: maxRoadLinkCount,
  maxRoadLinkPointCount: maxRoadLinkPointCount,
  maxRoadLinkIndexCount: maxRoadLinkIndexCount,
  maxRoadCount: maxRoadCount,
  maxAddressCount: maxAddressCount,

  quadtreeLeft: quadtreeLeft,
  quadtreeTop: quadtreeTop,
  quadtreeSize: quadtreeSize,

  // Inner Circle
  defaultCenterX: -122.2727,
  defaultCenterY: 37.8716,

  minZoom: 0,
  actualZoom: 2,
  defaultZoom: 7,
  maxZoom: 9,

  minLoaderPostingCount: 256,
  maxLoaderPostingCount: 1024,
  maxLoaderPostingDelay: 1000,

  textureSize: 1024,
  textureDataSize: 1024 * 1024
};

// NOTE: We assume textureDataSize >= maxRoadNodeCount + maxRoadLinkCount
