---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/add-clustergenericapplicationrole?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-ClusterGenericApplicationRole
---

# 添加通用集群应用程序角色（Add-ClusterGenericApplicationRole）

## 摘要
为原本并非为在故障转移集群中运行而设计的应用程序配置高可用性。

## 语法

```
Add-ClusterGenericApplicationRole -CommandLine <String> [-Parameters <String>]
 [-CheckpointKey <StringCollection>] [-Storage <StringCollection>]
 [-StaticAddress <StringCollection>] [-IgnoreNetwork <StringCollection>] [[-Name] <String>]
 [-Wait <Int32>] [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

## 描述

`Add-ClusterGenericApplicationRole` cmdlet 用于为那些原本并未设计为在故障转移集群中运行的应用程序配置高可用性。

如果一个应用程序是以“通用应用程序”（Generic Application）的身份运行的，那么集群软件将会启动该应用程序，并定期查询操作系统以确认该应用程序是否仍在运行。如果确认其在运行中，那么系统就会认为该应用程序处于在线状态，因此不会重新启动它，也不会将其切换到其他节点上（即不会发生故障转移）。

> [注意] > 如果服务器计算机上没有启用凭据安全服务提供程序（CredSSP）进行身份验证，就无法远程运行此cmdlet。

## 示例

#### 示例 1：将一个应用程序配置为通用的集群应用程序

```powershell
Add-ClusterGenericApplicationRole -CommandLine NewApplication.exe
```

这个示例将 `NewApplication.exe` 配置为一个通用的集群应用程序。客户端访问会使用一个默认名称，而且该应用程序不需要任何存储空间。

### 示例 2：配置一个具有存储功能的应用程序并为其命名

```powershell
$parameters = @{
    CommandLine = 'NewApplication.exe'
    Storage = 'Cluster Disk 4'
    Name = 'NewApplication'
}
Add-ClusterGenericApplicationRole @parameters
```

此示例将 `NewApplication.exe` 配置为使用 Cluster Disk 4 的通用集群应用程序，并为其指定名称 “NewApplication”。该示例通过“Splatting”机制将 `$Parameters` 变量中的参数值传递给命令。有关 [Splatting](/powershell/module/microsoft.powershell.core/about/about_splatting) 的更多信息，请参阅相关文档。

### 示例 3：配置应用程序以无需等待资源即可运行

```powershell
Add-ClusterGenericApplicationRole -CommandLine NewApplication.exe -Wait 0
```

这个示例将 `NewApplication.exe` 配置为一个通用的集群应用程序，并为其指定名称 “NewApplication”。该 cmdlet 会在不等待所有资源都上线的情况下完成配置过程。

## 参数

### -CheckpointKey

指定一个由逗号分隔的注册表检查点键列表，用于此高可用性通用应用程序。所有注册表路径均相对于 HKEY_LOCAL_MACHINE。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Cluster

指定要运行此 cmdlet 的集群名称。如果该参数的输入值为 `.` 或被省略，则 cmdlet 将在本地集群上运行。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CommandLine

指定用于高可用性通用应用程序的 Windows PowerShell 命令行。如果指定了完整路径，则当前目录会从 Windows PowerShell 命令行中自动解析出来。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IgnoreNetwork

指定在运行该 cmdlet 时需要忽略的一个或多个网络。启用了 DHCP 的网络总是会被包含在内，但其他网络需要使用 **StaticAddress** 参数来指定静态地址，或者应该通过 **IgnoreNetwork** 参数明确地将其忽略。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定用于创建高可用性应用程序的集群。

```yaml
Type: PSObject
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name

指定要创建的高可用性应用程序的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Parameters

指定用于高可用性通用应用程序的参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StaticAddress

指定一个或多个在运行此cmdlet时使用的静态地址。启用DHCP的网络始终会被包含在内，但其他网络需要通过**StaticAddress**参数来指定静态地址；或者可以使用**IgnoreNetwork**参数明确忽略这些网络。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Storage

指定要添加到所创建的高可用性应用程序中的集群磁盘资源。

```yaml
Type: StringCollection
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Wait

指定等待该cmdlet完成所需的时间（以秒为单位）。如果未指定**Wait**参数，那么cmdlet会一直等待直到操作完成；如果指定了值`0`，则命令会被立即执行，且cmdlet会在不等待的情况下返回结果。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft FailoverClusters PowerShell Cluster

## 输出

### MicrosoftFailoverClusters.PowerShellClusterGroup

## 备注

## 相关链接

[Add-ClusterGenericScriptRole](./Add-ClusterGenericScriptRole.md)

[Add-ClusterGenericServiceRole](./Add-ClusterGenericServiceRole.md)

[Get-ClusterGroup](./Get-ClusterGroup.md)

[Move-ClusterGroup](./Move-ClusterGroup.md)

[Remove-ClusterGroup](./Remove-ClusterGroup.md)

[启动集群组](./Start-ClusterGroup.md)

[Stop-ClusterGroup](./Stop-ClusterGroup.md)
