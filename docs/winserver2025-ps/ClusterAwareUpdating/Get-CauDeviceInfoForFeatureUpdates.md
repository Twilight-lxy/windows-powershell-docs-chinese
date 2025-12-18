---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: ClusterAwareUpdating.dll-Help.xml
Module Name: ClusterAwareUpdating
ms.date: 07/01/2024
online version: https://learn.microsoft.com/powershell/module/clusterawareupdating/get-caudeviceinfoforfeatureupdates?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-CauDeviceInfoForFeatureUpdates
---

# 获取用于功能更新的设备信息

## 摘要
从指定的目录中检索设备信息，以便进行功能更新。

## 语法

```
Get-CauDeviceInfoForFeatureUpdates [[-ClusterName] <String>] [-Credential <PSCredential>]
 -PathToDirectory <String> [-PathToDeploymentCab <String>] [<CommonParameters>]
```

## 描述

`Get-CauDeviceInfoForFeatureUpdates` cmdlet 从指定的目录中检索用于功能更新的设备信息。

## 示例

### 示例 1

```powershell
$parameters = @{
ClusterName = "CONTOSO-FC1"
PathToDirectory = "C:\Updates" 
PathToDeploymentCab = "C:\Deployment\FeatureUpdate.cab"
}
Get-CauDeviceInfoForFeatureUpdates $parameters
```

此命令从名为**CONTOSO-FC1**的集群的`C:\Updates`目录中检索用于功能更新的设备信息。同时，它还指定了用于存储更新内容的部署文件包（cab文件）的路径，该文件将保存在`C:\Deployment\FeatureUpdate.cab`中。

## 参数

### -ClusterName

指定用于创建 CAU 集群角色的集群名称。此参数仅在以下情况下需要：要么该 cmdlet 不在故障转移集群节点上运行；要么该 cmdlet 用于引用与执行该 cmdlet 的位置不同的故障转移集群。

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

### -Credential

指定目标集群的管理凭据。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PathToDeploymentCab

指定用于更新操作的部署包文件的路径。该部署包文件将会被创建出来。

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

### -PathToDirectory

指定包含设备信息文件的目录的路径。此参数是必需的。

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

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### 无

## 输出

### System.String

### Microsoft_clusterAwareUpdatingActivityIdMap

## 备注

## 相关链接
