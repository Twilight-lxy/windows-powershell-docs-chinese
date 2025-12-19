---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/remove-iscsiservertarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-IscsiServerTarget
---

# 删除IscsiServerTarget

## 摘要
删除指定的iSCSI目标。

## 语法

### TargetName（默认值）
```
Remove-IscsiServerTarget [-TargetName] <String> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

### InputObject
```
Remove-IscsiServerTarget -InputObject <IscsiServerTarget> [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

## 描述
`Remove-IscsiServerTarget` cmdlet 用于删除一个 iSCSI 目标对象。目标对象被删除后，iSCSI 发起程序将无法访问该虚拟磁盘。

## 示例

#### 示例 1：移除一个目标
```
PS C:\> Remove-IscsiServerTarget -Targetname "TargetOne"
```

这个示例会删除本地服务器上名为“TargetOne”的目标对象。

### 示例 2：删除服务器上的所有目标
```
PS C:\> $all = Get-IscsiServerTarget
PS C:\> ForEach-Object -InputObject ($each in $all) -Process {Remove-IscsiServerTarget -InputObject $each}
```

这个示例会删除本地服务器上的所有目标对象。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定远程计算机的名称或 IP 地址。

指定集群资源组的网络名称，或者如果此cmdlet在集群配置上运行，则指定集群节点的名称。

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

### -InputObject
从输入管道中接收一个 iSCSI 目标对象。

```yaml
Type: IscsiServerTarget
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetName
指定 iSCSI 目标的名称。

```yaml
Type: String
Parameter Sets: TargetName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Iscsi.Target Commands.IscsiServerTarget

## 输出

### 无

## 备注

## 相关链接

[ForEach-Object](https://go.microsoft.com/fwlink/p/?Linkd=113300)

[Get-IscsiServerTarget](./Get-IscsiServerTarget.md)

[New-IscsiServerTarget](./New-IscsiServerTarget.md)

[Set-IscsiServerTarget](./Set-IscsiServerTarget.md)

