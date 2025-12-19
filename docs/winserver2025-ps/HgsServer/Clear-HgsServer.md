---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsServer-help.xml
Module Name: HgsServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsserver/clear-hgsserver?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-HgsServer
---

# Clear-HgsServer

## 摘要
将本地节点上的Host Guardian服务重置为未初始化的状态。

## 语法

```
Clear-HgsServer [[-ClusterName] <String>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Clear-HgsServer` 这个 cmdlet 用于将本地节点从 Host Guardian Service (HGS) 中删除。

此cmdlet会在额外的HGS节点上执行以下基础设施组件更改：

- Unregisters the Attestation service web application with the IIS service.
- Unregisters the Key Protection service web application with the IIS service.
- Disables Just Enough Administration on the local node.
- Removes the local node from the existing failover cluster.

This cmdlet makes the following infrastructure components changes on the last HGS node:

- Unregisters the Attestation service web application with the IIS service.
- Unregisters the Key Protection service web application with the IIS service.
- Removes the Distributed Network Name resource corresponding to the Host Guardian Service name.
- Disables Just Enough Administration on the local node.
- Destroys the cluster on the local node.

有关场景术语的更多信息，请参阅[安全性和保障措施](https://go.microsoft.com/fwlink/?LinkId=699209)。

## 示例

### 示例 1：清除本地节点上的所有集群初始化设置
```
PS C:\> Clear-HgsServer
```

此命令会将本地节点上的HGS服务器恢复到初始状态（即“干净”状态），以便为其后续执行**Initialize-HgsServer**命令做好准备。

### 示例 2：在未经确认的情况下，清除本地节点上的所有集群初始化设置
```
PS C:\> Clear-HgsServer -Force -Confirm:$False
```

该命令会将本地节点上的HGS服务器恢复到初始状态（即“干净”状态），以便后续执行**Initialize-HgsServer**命令。在执行此命令时，系统不会要求用户进行确认。

## 参数

### -ClusterName
指定一个集群名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令执行，而不会询问用户的确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[HGS 服务器Cmdlets](./hgsserver.md)

[Initialize-HgsServer](./Initialize-HgsServer.md)

