/* eslint-env jest */

import { shallowMount } from "@vue/test-utils";
import HomeView from "../src/views/HomeView.vue";

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () =>
      Promise.resolve({
        articles: [
          {
            title: "Top News 1",
            urlToImage: "https://example.com/image1.jpg",
            content: "Sample content for news 1",
            description: "Description for news 1",
          },
          {
            title: "Top News 2",
            urlToImage: "https://example.com/image2.jpg",
            content: "Sample content for news 2",
            description: "Description for news 2",
          },
        ],
      }),
  })
);

describe("HomeView.vue", () => {
  let wrapper;
  beforeEach(() => {
    wrapper = shallowMount(HomeView);
  });

  it("renders carousel with top news", async () => {
    await wrapper.vm.getTopNewsData();
    expect(wrapper.vm.data.length).toBe(2);
    expect(wrapper.findAll(".carousel-item").length).toBe(2);
  });

  it("opens a dialog when a carousel item is clicked", async () => {
    await wrapper.vm.getTopNewsData();
    wrapper.find(".carousel-item").trigger("click");
    expect(wrapper.vm.dialogVisible).toBe(true);
  });
});
