const desks = {
  AS: ['Asia', '#734637'], NA: ['N. America', '#884238'],
  SA: ['S. America', '#895018'], EU: ['Europe', '#315884'],
  AF: ['Africa', '#49652e'], OC: ['Oceania', '#246961'], SP: ['Space', '#454879'],
};

function element(tag, klass, text) {
  const node = document.createElement(tag);
  if (klass) node.className = klass;
  if (text !== undefined) node.textContent = text;
  return node;
}

function makeStory(data, index) {
  const [place, region, , , headline, deck, art] = data;
  const isBrief = index >= 13;
  const wrapper = element(isBrief ? 'li' : 'article', 'story');
  wrapper.style.setProperty('--desk', desks[region][1]);
  wrapper.dataset.story = String(index + 1);
  if (isBrief) {
    wrapper.append(element('strong', 'brief-place', place + ' · '), document.createTextNode(headline));
    return wrapper;
  }
  const meta = element('div', 'meta');
  if (index < 3) {
    const scene = element('div', 'scene');
    scene.innerHTML = artwork(art, true);
    wrapper.append(scene);
  } else {
    const icon = element('span', 'icon');
    icon.setAttribute('aria-hidden', 'true');
    icon.innerHTML = deskIcon(art, desks[region][1]);
    meta.append(icon);
  }
  meta.append(element('span', null, place));
  wrapper.append(meta, element('h2', null, headline), element('p', 'deck', deck));
  return wrapper;
}

const sections = [...document.querySelectorAll('.lead, .mid, .briefs')];
stories.forEach((story, index) => sections[index < 3 ? 0 : index < 13 ? 1 : 2].append(makeStory(story, index)));
document.querySelector('.edition-count').textContent = `${stories.length} STORIES / 6 CONTINENTS`;
