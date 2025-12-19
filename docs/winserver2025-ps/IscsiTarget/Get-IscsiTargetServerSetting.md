---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/get-iscsitargetserversetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IscsiTargetServerSetting
---

# 获取 iSCSI 目标服务器设置

## 摘要
用于获取iSCSI目标、虚拟磁盘或快照的全局设置或通用配置信息。

## 语法

```
Get-IscsiTargetServerSetting [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Get-IscsiTargetServerSetting` cmdlet 可以获取 iSCSI 目标、虚拟磁盘或快照的全局设置或通用配置信息。

## 示例

### 示例 1：获取本地计算机的门户条目
```
PS C:\> Get-IscsiTargetServerSetting
ComputerName                            Version                                 Portals
------------                            -------                                 -------
fssvr.contoso.com                       6.3.9600                                {+172.21.0.1:3260, ...
```

这个示例获取了本地服务器上的所有门户条目信息。

## 参数

### -ComputerName
如果此cmdlet在远程计算机上运行，则会指定远程计算机的名称或IP地址。

指定集群资源组的网络名称；或者如果此cmdlet在集群配置上运行，则指定集群节点的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Credential
指定在连接到远程计算机时所需的凭据信息。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Set-IscsiTargetServerSetting](./Set-IscsiTargetServerSetting.md)

