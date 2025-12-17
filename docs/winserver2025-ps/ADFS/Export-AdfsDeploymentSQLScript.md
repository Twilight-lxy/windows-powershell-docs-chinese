---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/export-adfsdeploymentsqlscript?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-AdfsDeploymentSQLScript
---

# Export-AdfsDeploymentSQLScript

## 摘要
生成SQL脚本，用于创建AD FS数据库并授予相应的权限。

## 语法

```
Export-AdfsDeploymentSQLScript -DestinationFolder <String> -ServiceAccountName <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Export-AdfsDeploymentSQLScript` cmdlet 用于生成 SQL 脚本，您可以分别使用这些脚本来创建 Active Directory Federation Services (AD FS) 数据库以及授予相应的权限。

## 示例

#### 示例 1：导出 SQL 部署脚本
```
PS C:\> Export-AdfsDeploymentSQLScript -DestinationFolder ".\ScriptFolder" -ServiceAccountName "ContosoDomain\PattiFuller"
```

此命令代表指定的 AD FS 服务账户导出用于 AD FS 安装的 SQL 部署脚本。

## 参数

### -DestinationFolder
指定cmdlet将生成的SQL脚本保存到的文件夹。

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

### -ServiceAccountName
指定运行 AD FS 服务的 Active Directory® 域服务账户的名称。该集群中的所有节点必须使用相同的 서비스 계정（service account）。

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

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

