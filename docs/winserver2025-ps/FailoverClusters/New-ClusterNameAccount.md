---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.FailoverClusters.PowerShell.dll-Help.xml
Module Name: FailoverClusters
ms.date: 11/22/2022
online version: https://learn.microsoft.com/powershell/module/failoverclusters/new-clusternameaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-ClusterNameAccount
---

# 新集群名称账户

## 摘要
在 Active Directory 域服务中创建一个用于管理集群名称的账户。

## 语法

### InputObject（默认值）

```
New-ClusterNameAccount -Name <String> [-Credentials <PSCredential>] [-Domain <String>]
 [-InputObject <PSObject>] [-Cluster <String>] [<CommonParameters>]
```

### 凭证（Credentials）

```
New-ClusterNameAccount -Name <String> -Credentials <PSCredential> -Domain <String>
 [-Cluster <String>] [<CommonParameters>]
```

## 描述

`New-ClusterNameAccount` cmdlet 在 Active Directory Domain Services 中创建一个集群名称账户。这种集群名称账户也被称为集群名称对象（Cluster Name Object，简称 CNO）。该 cmdlet 会更改现有的集群名称，使其与所创建的集群名称账户相匹配。如果某个集群已经存在对应的集群名称账户，则该 cmdlet 不会产生任何效果。

## 示例

#### 示例 1：为当前集群创建一个集群名称账户

```powershell
New-ClusterNameAccount -Name "cluster_17" -Domain "production.contoso.com"
```

此命令会为当前集群在指定的域中创建一个集群名称账户。当前集群是执行此 cmdlet 时所针对的默认集群。

### 示例 2：使用凭据创建集群名称账户

```powershell
$Credential = Get-Credential
New-ClusterNameAccount -Name "cluster27" -Domain "production.contoso.com" -Credentials $Credential
```

第一个命令会提示您输入凭据，然后将这些凭据存储在 `$Credential` 变量中。

第二个命令为当前集群在指定的域中创建一个集群名称账户。该命令使用了存储在 `$Credential` 变量中的凭据来访问 Active Directory 域服务。

## 参数

### -Cluster

指定要运行此cmdlet的集群名称。如果该参数的值为`.`或被省略，则cmdlet将在本地集群上运行。

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

指定此 cmdlet 在连接到 Active Directory 域服务时使用的凭据。若要获取凭据，请使用 `Get-Credential` cmdlet。有关更多信息，请键入 `Get-Help Get-Credential`。

```yaml
Type: PSCredential
Parameter Sets: InputObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: PSCredential
Parameter Sets: Credentials
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Domain

指定此cmdlet用于创建集群名称账户的Active Directory域服务域名。

```yaml
Type: String
Parameter Sets: InputObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: Credentials
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject

指定该 cmdlet 用于为其添加集群名称账户的集群。

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

### -Name

指定此cmdlet创建的集群账户的名称。

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

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftFailoverClusters.PowerShellCluster

此cmdlet接受一个**Cluster**对象，并为此对象创建一个集群名称账户。

## 输出

## 备注

## 相关链接

[获取凭据](https://go.microsoft.com/fwlink/?LinkID=293936)
