import { AngularProjectScratchPage } from './app.po';

describe('angular-project-scratch App', function() {
  let page: AngularProjectScratchPage;

  beforeEach(() => {
    page = new AngularProjectScratchPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
