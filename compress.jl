using Images, LinearAlgebra, MultivariateStats, FileIO

function apply_pca_and_reduce(image_matrix, variance_threshold)
    mean_vector = mean(image_matrix, dims=2)
    centered_data = image_matrix .- mean_vector

    pca = fit(PCA, centered_data; maxoutdim=size(centered_data, 1))

    explained_variance = cumsum(pca.prinvars) / sum(pca.prinvars)

    n_components = findfirst(explained_variance .>= variance_threshold)

    reduced_data = transform(pca, centered_data)
    reduced_data = reduced_data[1:n_components, :]


function apply_pca_and_reduce(image_matrix, variance_threshold)
    mean_vector = mean(image_matrix, dims=2)
    centered_data = image_matrix .- mean_vector

    pca = fit(PCA, centered_data; maxoutdim=size(centered_data, 1))

    explained_variance = cumsum(pca.prinvars) / sum(pca.prinvars)

    n_components = findfirst(explained_variance .>= variance_threshold)

    reduced_data = transform(pca, centered_data)
    reduced_data = reduced_data[1:n_components, :]

    reconstructed_data = reconstruct(pca, reduced_data)
    reconstructed_data .+= mean_vector

    return reconstructed_data
end

function main()
    image_path = "input_image.jpg"  # Substitua pelo caminho da sua imagem
    image = load(image_path)

    image_matrix = Float32.(channelview(image))

    variance_threshold = 0.95

    reduced_image_matrix = apply_pca_and_reduce(image_matrix, variance_threshold)

    reduced_image = colorview(RGB, reduced_image_matrix)

    output_path = "output_image.jpg"  # Substitua pelo caminho de saída desejado
    save(output_path, reduced_image)

    println("Imagem processada e salva em $output_path")
end

main()
    reconstructed_data .+= mean_vector

    return reconstructed_data
end

function main()
    image_path = "input_image.jpg"
    image = load(image_path)

    image_matrix = Float32.(channelview(image))

    variance_threshold = 0.95

    reduced_image_matrix = apply_pca_and_reduce(image_matrix, variance_threshold)

    reduced_image = colorview(RGB, reduced_image_matrix)

    output_path = "output_image.jpg"
    save(output_path, reduced_image)

    println("Imagem processada e salva em $output_path")
end

main()