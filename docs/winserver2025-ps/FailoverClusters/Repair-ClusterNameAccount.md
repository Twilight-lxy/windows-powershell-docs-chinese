---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 08/28/2024
online version: https://learn.microsoft.com/powershell/module/failoverclusters/repair-clusternameaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Repair-ClusterNameAccount
---

# 修复-集群名称-账户

## 摘要
修复集群名称相关的账户问题，并确保集群能够继续正常运行。

## 语法

### InputObject（默认值）

```
Repair-ClusterNameAccount [-Credentials <PSCredential>] [-Domain <String>] [-InputObject <PSObject>]
 [-Cluster <String>] [<CommonParameters>]
```

### 凭据（Credentials）

```
Repair-ClusterNameAccount [-Credentials <PSCredential>] [-Domain <String>] [-Cluster <String>]
 [<CommonParameters>]
```

## 描述

`Repair-ClusterNameAccount` cmdlet 用于修复或更新用于故障转移集群（Failover Cluster）中身份验证和授权的“集群名称账户”（Cluster Name Account）。该账户用于在集群中创建高可用性应用程序（Highly Available Applications）或虚拟计算机对象（Virtual Computer Objects，简称 VCOs）。

要了解更多关于域环境中集群账户的信息，请参阅[在Active Directory中配置集群账户](/windows-server/failover-clustering/configure-ad-accounts)。

## 示例

### 示例 1

```powershell
Repair-ClusterNameAccount -Cluster "Cluster01"
```

这个示例用于修复或更新名为`Cluster01`的集群的“Cluster Name Account”（集群名称账户）。

### 示例 2

```powershell
$cred = Get-Credential
Repair-ClusterNameAccount -Cluster "Cluster01" -Credentials $cred -Domain "contoso.com"
```

这个示例使用指定的凭据和域名来修复或更新名为 `Cluster01` 的集群的集群名称账户。`Get-Credential` cmdlet 用于为 `-Credentials` 参数创建一个 PSCredential 对象。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的输入值为`.`或被省略，则cmdlet将在本地集群上运行。

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

### -Credentials

指定此cmdlet在连接到Active Directory域服务时使用的凭据。

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

### -Domain

指定用于修复集群名称账户的域的名称。这应该是该集群所在域的完全限定域名（FQDN）。

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

### -InputObject

指定要修复的集群名称和账户信息。

```yaml
Type: PSObject
Parameter Sets: InputObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](/powershell/module/microsoft.powershell.core/about/about_commonparameters)。

## 输入

### System.ManagementAutomation.PSObject

## 输出

### System.Object

## 备注

## 相关链接

[Add-ClusterExcludedAdapter](add-clusterexcludedadapter.md)

[Get-ClusterExcludedAdapter](get-clusterexcludedadapter.md)

[Remove-ClusterExcludedAdapter](remove-clusterexcludedadapter.md)

[Set-ClusterExcludedAdapter](set-clusterexcludedadapter.md)
