package com.example.ecommerce.repository.datasource

import com.example.ecommerce.model.Category
import com.example.ecommerce.model.Slider
import com.example.ecommerce.network.ApiService
import io.reactivex.rxjava3.core.Single

class RemoteCategoryDataSource(
    private val apiService: ApiService
) : CategoryDataSource {
    override fun category(): Single<List<Category>> = apiService.category()


}