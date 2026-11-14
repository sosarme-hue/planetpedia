<?php
/* IApedia · Vídeos actuales sobre IA en español.
 * Lee los vídeos recientes de una lista de canales de YouTube (feeds públicos, sin clave),
 * se queda con los que tratan de IA y los ordena por visitas. Se renueva como mucho cada 12 horas. */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=3600');

$CACHE = sys_get_temp_dir() . '/iapedia-videos-v1.json';
$TTL = 12 * 3600;

if (is_file($CACHE) && (time() - filemtime($CACHE)) < $TTL) { readfile($CACHE); exit; }

// [id del canal, nombre, ¿todo es de IA?]
$CANALES = [
  ['UCy5znSnfMsDwaLlROnZ7Qbg', 'Dot CSV', true],
  ['UCX_dT6nVtCIHRo_GFOsWK2A', 'Migue Baena IA', true],
  ['UCVt4ugq2txl_szlXAO7B3-g', 'Adrián Sáenz', false],
  ['UCHsO9q47lb3mp0lgzdtvySw', 'Pau Rodríguez', true],
  ['UCsDXXCoXaS-wO1Wnnt_LM3A', 'CenteIA Education', true],
  ['UCl5-lvQyfILb-l2abPk4Ntg', 'Inteligencia Artificial', true],
  ['UC36xmz34q02JYaZYKrMwXng', 'Nate Gentile', false],
  ['UC55-mxUj5Nj3niXFReG44OQ', 'Platzi', false],
  ['UCm9QZ70KuIVShztZ7HmE4NQ', 'Ringa Tech', false],
  ['UCH-Z8ya93m7_RD02WsCSZYA', 'Derivando', false],
  ['UCaRLjOy-9m_eJ9REVqc0YoQ', 'Gustavo Entrala', false],
  ['UCUBIrDsIVzRpKsClMlSlTpQ', 'BBC News Mundo', false],
  ['UCGdlvijxkue8x5AyBrBUljQ', 'ChicaGeek', false],
  ['UC-x6wApVHX17BgP696Q0K9g', 'Founderz', false],
  ['UCzfyW6wo2Q123IqMKe7B_Qw', 'Alan Daitch', false],
];
$PATRON = '/(\bIA\b|\bAI\b|inteligencia artificial|chat ?gpt|\bGPT|gemini|claude|copilot|openai|anthropic|deepseek|\bllama\b|\bgrok\b|agentes? de|\bsora\b|midjourney|prompt|\bLLM|perplexity|notebooklm|machine learning|redes? neuronal|robot)/iu';
$FUERA = '/(dinero|millonari|\\brico\\b|ricos|numerolog|dropshipping|negocio|compra-venta|criptomoneda)/iu';
$DIAS = 45;
$MESES = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];

function traer($url) {
  if (function_exists('curl_init')) {
    $c = curl_init($url);
    curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 8, CURLOPT_FOLLOWLOCATION => true, CURLOPT_USERAGENT => 'IApedia/1.0']);
    $r = curl_exec($c); $ok = curl_getinfo($c, CURLINFO_HTTP_CODE) == 200; curl_close($c);
    return $ok ? $r : false;
  }
  return @file_get_contents($url);
}

$videos = [];
foreach ($CANALES as [$id, $nombre, $todoIA]) {
  $xml = traer('https://www.youtube.com/feeds/videos.xml?channel_id=' . $id);
  if (!$xml) continue;
  $feed = @simplexml_load_string($xml);
  if (!$feed) continue;
  foreach ($feed->entry as $e) {
    $yt = $e->children('http://www.youtube.com/xml/schemas/2015');
    $media = $e->children('http://search.yahoo.com/mrss/');
    $titulo = (string)$e->title;
    $enlace = (string)$e->link['href'];
    if (strpos($enlace, '/shorts/') !== false) continue;
    $pub = strtotime((string)$e->published);
    if (!$pub || $pub < time() - $DIAS * 86400) continue;
    if (!$todoIA && !preg_match($PATRON, $titulo)) continue;
    if (preg_match($FUERA, $titulo)) continue;
    $visitas = 0;
    if (isset($media->group->community->statistics)) $visitas = (int)$media->group->community->statistics->attributes()['views'];
    $videos[] = ['id' => (string)$yt->videoId, 'titulo' => $titulo, 'canal' => $nombre, 'visitas' => $visitas,
                 'fecha' => date('j', $pub) . ' de ' . $MESES[(int)date('n', $pub) - 1], 't' => $pub];
  }
}

if (!$videos) { // si YouTube no responde, se sirve la última lista buena
  if (is_file($CACHE)) { readfile($CACHE); exit; }
  echo json_encode(['videos' => []]); exit;
}
usort($videos, fn($a, $b) => $b['visitas'] <=> $a['visitas']);
$videos = array_slice($videos, 0, 24);
foreach ($videos as &$v) unset($v['t']);
$hoy = date('j') . ' de ' . $MESES[(int)date('n') - 1] . ' de ' . date('Y');
$json = json_encode(['actualizado' => $hoy, 'videos' => $videos], JSON_UNESCAPED_UNICODE);
@file_put_contents($CACHE, $json, LOCK_EX);
echo $json;
