---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Deployment.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsfarmnode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsFarmNode
---

# 移除 AdfsFarmNode

## 摘要
`Remove-AdfsFarmNode` cmdlet 已被弃用。请改用 `Uninstall-WindowsFeature` cmdlet。

## 语法

### ADFSRemoveFarmNodeDefault（默认值）
```
Remove-AdfsFarmNode -ServiceAccountCredential <PSCredential> [<CommonParameters>]
```

### AdfsRemoveFarmNodeGmsa
```
Remove-AdfsFarmNode -GroupServiceAccountIdentifier <String> [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
**Remove-AdfsFarmNode** cmdlet 在此版本中已被弃用。请改用 [Uninstall-WindowsFeature](https://go.microsoft.com/fwlink/?LinkID=287572) cmdlet。有关 **Uninstall-WindowsFeature** cmdlet 的更多信息，请输入 `Get-Help Uninstall-WindowsFeature`。需要注意的是，**Uninstall-WindowsFeature** cmdlet 仅会删除服务器角色，并不会将相关节点从 ADFS 架构中移除。要进行彻底清理，请使用带有 `-RemoveNode` 参数的 **Set-AdfsFarmInformation** cmdlet。

## 示例

## 参数

### -Credential
```yaml
Type: PSCredential
Parameter Sets: AdfsRemoveFarmNodeGmsa
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GroupServiceAccountIdentifier
```yaml
Type: String
Parameter Sets: AdfsRemoveFarmNodeGmsa
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ServiceAccountCredential
```yaml
Type: PSCredential
Parameter Sets: ADFSRemoveFarmNodeDefault
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Uninstall-WindowsFeature](/powershell/module/servermanager/uninstall-windowsfeature)

